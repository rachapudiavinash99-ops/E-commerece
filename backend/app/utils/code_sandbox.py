import ast
import io
import sys
import time
import traceback
from typing import Any, Dict, List, Optional, Tuple


class SafeCodeRunner:
    FORBIDDEN_MODULES = {"os", "sys", "subprocess", "socket", "urllib", "shutil", "pathlib", "ctypes"}
    FORBIDDEN_BUILTINS = {"exec", "eval", "compile", "open", "__import__", "globals", "locals"}

    @classmethod
    def analyze_safety(cls, code: str) -> Tuple[bool, Optional[str]]:
        """AST check for dangerous operations."""
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            return False, f"Syntax Error: {e.msg} at line {e.lineno}"

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.split(".")[0] in cls.FORBIDDEN_MODULES:
                        return False, f"Security Warning: Import of module '{alias.name}' is prohibited in the sandbox."
            elif isinstance(node, ast.ImportFrom):
                if node.module and node.module.split(".")[0] in cls.FORBIDDEN_MODULES:
                    return False, f"Security Warning: Import from module '{node.module}' is prohibited in the sandbox."
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name) and node.func.id in cls.FORBIDDEN_BUILTINS:
                    return False, f"Security Warning: Calling '{node.func.id}()' is prohibited in the sandbox."
        return True, None

    @classmethod
    def execute_python_code(
        cls,
        code: str,
        test_cases: List[Dict[str, Any]],
        timeout_seconds: float = 3.0
    ) -> Dict[str, Any]:
        """Run code against test cases with output capture and error handling."""
        is_safe, error_msg = cls.analyze_safety(code)
        if not is_safe:
            return {
                "status": "syntax_error",
                "output": error_msg,
                "score": 0,
                "passed_test_cases": 0,
                "total_test_cases": len(test_cases),
                "execution_time_ms": 0.0,
                "details": error_msg
            }

        start_time = time.perf_counter()
        passed_count = 0
        total_cases = len(test_cases)
        last_output = ""
        status = "passed"
        details_list = []

        safe_globals = {
            "__builtins__": {
                "print": print, "range": range, "len": len, "int": int, "float": float,
                "str": str, "list": list, "dict": dict, "set": set, "tuple": tuple,
                "bool": bool, "abs": abs, "min": min, "max": max, "sum": sum,
                "sorted": sorted, "enumerate": enumerate, "zip": zip, "map": map,
                "filter": filter, "isinstance": isinstance, "round": round
            }
        }

        try:
            # First execute user definition code
            old_stdout = sys.stdout
            redirected_output = io.StringIO()
            sys.stdout = redirected_output

            local_scope: Dict[str, Any] = {}
            exec(code, safe_globals, local_scope)

            sys.stdout = old_stdout
            initial_out = redirected_output.getvalue().strip()

            if not test_cases:
                elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
                return {
                    "status": "passed",
                    "output": initial_out or "Execution completed successfully.",
                    "score": 10,
                    "passed_test_cases": 1,
                    "total_test_cases": 1,
                    "execution_time_ms": elapsed_ms,
                    "details": "Code executed with no errors."
                }

            # Run test cases
            for idx, tc in enumerate(test_cases):
                expected = str(tc.get("expected_output", "")).strip()
                input_data = tc.get("input_data", "")

                test_out_buf = io.StringIO()
                sys.stdout = test_out_buf

                try:
                    if input_data:
                        # If input is a function call or expression
                        eval_result = eval(input_data, safe_globals, local_scope)
                        actual_out = str(eval_result).strip()
                    else:
                        actual_out = initial_out

                    sys.stdout = old_stdout
                    test_printed = test_out_buf.getvalue().strip()
                    if test_printed and not actual_out:
                        actual_out = test_printed

                    last_output = actual_out

                    if actual_out == expected:
                        passed_count += 1
                        details_list.append(f"Test case #{idx+1}: PASSED")
                    else:
                        status = "failed"
                        details_list.append(f"Test case #{idx+1}: FAILED (Expected '{expected}', got '{actual_out}')")
                except Exception as ex:
                    sys.stdout = old_stdout
                    status = "runtime_error"
                    details_list.append(f"Test case #{idx+1}: ERROR - {str(ex)}")

        except SyntaxError as se:
            sys.stdout = sys.__stdout__
            return {
                "status": "syntax_error",
                "output": f"Syntax Error: {se.msg} on line {se.lineno}",
                "score": 0,
                "passed_test_cases": 0,
                "total_test_cases": total_cases,
                "execution_time_ms": 0.0,
                "details": str(se)
            }
        except Exception as e:
            sys.stdout = sys.__stdout__
            elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
            return {
                "status": "runtime_error",
                "output": f"Runtime Error: {str(e)}\n{traceback.format_exc()}",
                "score": 0,
                "passed_test_cases": 0,
                "total_test_cases": total_cases,
                "execution_time_ms": elapsed_ms,
                "details": str(e)
            }
        finally:
            sys.stdout = sys.__stdout__

        elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
        score = int((passed_count / total_cases) * 10) if total_cases > 0 else 10
        if passed_count == total_cases:
            status = "passed"

        return {
            "status": status,
            "output": last_output or "Tests completed.",
            "score": score,
            "passed_test_cases": passed_count,
            "total_test_cases": total_cases,
            "execution_time_ms": elapsed_ms,
            "details": "\n".join(details_list)
        }
