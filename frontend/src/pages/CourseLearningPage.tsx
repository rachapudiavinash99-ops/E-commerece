import React, { useEffect, useState } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { Course, Module, Lesson, CourseProgressState, TaskSubmissionResult, QuizAttemptResult } from '../types';
import { apiClient } from '../api/client';
import { 
  PlayCircle, CheckCircle2, Circle, ChevronLeft, ChevronRight, 
  Terminal, HelpCircle, Award, BookOpen, Download, Sparkles, Loader2, RefreshCw 
} from 'lucide-react';
import { Button } from '../components/common/Button';
import { Badge } from '../components/common/Badge';
import { Modal } from '../components/common/Modal';

export const CourseLearningPage: React.FC = () => {
  const { courseId } = useParams<{ courseId: string }>();
  const navigate = useNavigate();

  const [course, setCourse] = useState<Course | null>(null);
  const [curriculum, setCurriculum] = useState<Module[]>([]);
  const [progress, setProgress] = useState<CourseProgressState | null>(null);
  const [activeLesson, setActiveLesson] = useState<Lesson | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  // Coding task runner state
  const [userCode, setUserCode] = useState('');
  const [taskResult, setTaskResult] = useState<TaskSubmissionResult | null>(null);
  const [isSubmittingCode, setIsSubmittingCode] = useState(false);

  // Quiz state
  const [selectedAnswers, setSelectedAnswers] = useState<Record<number, number[]>>({});
  const [quizResult, setQuizResult] = useState<QuizAttemptResult | null>(null);
  const [isSubmittingQuiz, setIsSubmittingQuiz] = useState(false);

  // Certificate Modal
  const [isCertModalOpen, setIsCertModalOpen] = useState(false);
  const [certSvg, setCertSvg] = useState<string | null>(null);

  const fetchData = async () => {
    if (!courseId) return;
    try {
      const [cRes, curRes, progRes] = await Promise.all([
        apiClient.get<Course>(`/courses/detail/${courseId}`).catch(() => apiClient.get<Course>(`/courses`)),
        apiClient.get<Module[]>(`/curriculum/courses/${courseId}`),
        apiClient.get<CourseProgressState>(`/learning/courses/${courseId}`)
      ]);

      // Handle course matching
      const foundCourse = Array.isArray(cRes.data)
        ? (cRes.data as any).items?.find((c: any) => c.id === Number(courseId)) || cRes.data[0]
        : cRes.data;

      setCourse(foundCourse);
      setCurriculum(curRes.data);
      setProgress(progRes.data);

      // Set initial active lesson
      if (curRes.data.length > 0 && curRes.data[0].lessons.length > 0) {
        const firstLesson = curRes.data[0].lessons[0];
        setActiveLesson(firstLesson);
        if (firstLesson.coding_tasks && firstLesson.coding_tasks.length > 0) {
          setUserCode(firstLesson.coding_tasks[0].starter_code || '');
        }
      }
    } catch (err) {
      console.error('Failed to load learning room', err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, [courseId]);

  const selectLesson = (lesson: Lesson) => {
    setActiveLesson(lesson);
    setTaskResult(null);
    setQuizResult(null);
    setSelectedAnswers({});
    if (lesson.coding_tasks && lesson.coding_tasks.length > 0) {
      setUserCode(lesson.coding_tasks[0].starter_code || '');
    }
  };

  const markCurrentLessonComplete = async () => {
    if (!activeLesson) return;
    try {
      const res = await apiClient.post(`/learning/lessons/${activeLesson.id}/complete`, {
        completed: true,
        watched_seconds: activeLesson.duration_minutes * 60
      });
      setProgress(res.data);

      // Auto-advance to next lesson if available
      advanceToNextLesson();
    } catch (e) {
      console.error(e);
    }
  };

  const advanceToNextLesson = () => {
    if (!activeLesson) return;
    let foundCurrent = false;
    for (const mod of curriculum) {
      for (const les of mod.lessons) {
        if (foundCurrent) {
          selectLesson(les);
          return;
        }
        if (les.id === activeLesson.id) {
          foundCurrent = true;
        }
      }
    }
  };

  const advanceToPrevLesson = () => {
    if (!activeLesson) return;
    let prev: Lesson | null = null;
    for (const mod of curriculum) {
      for (const les of mod.lessons) {
        if (les.id === activeLesson.id && prev) {
          selectLesson(prev);
          return;
        }
        prev = les;
      }
    }
  };

  // Submit code to backend runner
  const handleRunCode = async (taskId: number) => {
    setIsSubmittingCode(true);
    try {
      const res = await apiClient.post<TaskSubmissionResult>('/tasks/submit', {
        task_id: taskId,
        code: userCode
      });
      setTaskResult(res.data);
      if (res.data.status === 'passed') {
        markCurrentLessonComplete();
      }
    } catch (err: any) {
      console.error(err);
    } finally {
      setIsSubmittingCode(false);
    }
  };

  // Submit quiz answers
  const handleSubmitQuiz = async (quizId: number) => {
    setIsSubmittingQuiz(true);
    try {
      const res = await apiClient.post<QuizAttemptResult>('/quizzes/submit', {
        quiz_id: quizId,
        answers: selectedAnswers
      });
      setQuizResult(res.data);
      if (res.data.passed) {
        markCurrentLessonComplete();
      }
    } catch (err) {
      console.error(err);
    } finally {
      setIsSubmittingQuiz(false);
    }
  };

  const handleOpenCertificate = async () => {
    if (!progress?.certificate_id) {
      // Generate if eligible
      try {
        const certListRes = await apiClient.get('/certificates');
        const match = certListRes.data.find((c: any) => c.course_id === Number(courseId));
        if (match) {
          setCertSvg(match.svg_content);
          setIsCertModalOpen(true);
        }
      } catch (e) {}
      return;
    }
    try {
      const res = await apiClient.get(`/certificates/${progress.certificate_id}/svg`);
      setCertSvg(res.data);
      setIsCertModalOpen(true);
    } catch (e) {
      setIsCertModalOpen(true);
    }
  };

  if (isLoading || !activeLesson) {
    return (
      <div className="flex items-center justify-center min-h-[70vh]">
        <Loader2 className="w-8 h-8 text-brand-400 animate-spin" />
      </div>
    );
  }

  const isCurrentLessonDone = progress?.completed_lesson_ids.includes(activeLesson.id);

  return (
    <div className="flex flex-col h-[calc(100vh-4rem)] bg-slate-950 overflow-hidden">
      {/* Top Learning Bar */}
      <div className="h-14 border-b border-slate-800 bg-slate-900/90 px-6 flex items-center justify-between flex-shrink-0">
        <div className="flex items-center gap-3">
          <Link to="/student/dashboard" className="p-1.5 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors">
            <ChevronLeft className="w-5 h-5" />
          </Link>
          <span className="font-bold text-sm text-slate-100 line-clamp-1">{course?.title || 'Learning Course'}</span>
        </div>

        {/* Progress Bar & Certificate */}
        <div className="flex items-center gap-4">
          <div className="hidden sm:flex items-center gap-2">
            <div className="w-32 bg-slate-800 rounded-full h-2 overflow-hidden">
              <div
                className="bg-gradient-to-r from-brand-500 to-emerald-400 h-2 transition-all duration-500"
                style={{ width: `${progress?.completion_percentage || 0}%` }}
              />
            </div>
            <span className="text-xs font-bold text-slate-300">{progress?.completion_percentage || 0}%</span>
          </div>

          {(progress?.completion_percentage || 0) >= 100 && (
            <Button
              size="sm"
              variant="success"
              onClick={handleOpenCertificate}
              leftIcon={<Award className="w-4 h-4 text-amber-300" />}
            >
              Get Certificate
            </Button>
          )}
        </div>
      </div>

      {/* Main Learning Workspace (2 Columns) */}
      <div className="flex-1 flex flex-col lg:flex-row overflow-hidden">
        {/* Left / Center: Interactive Content Area */}
        <div className="flex-1 flex flex-col overflow-y-auto bg-slate-950 p-6 space-y-6">
          {/* Header of Active Lesson */}
          <div className="flex items-center justify-between">
            <div className="space-y-1">
              <span className="text-xs font-bold uppercase tracking-wider text-brand-400">
                {activeLesson.lesson_type.replace('_', ' ')}
              </span>
              <h2 className="text-2xl font-bold text-white tracking-tight">{activeLesson.title}</h2>
            </div>

            <Button
              variant={isCurrentLessonDone ? 'success' : 'secondary'}
              size="sm"
              onClick={markCurrentLessonComplete}
              leftIcon={isCurrentLessonDone ? <CheckCircle2 className="w-4 h-4" /> : <Circle className="w-4 h-4" />}
            >
              {isCurrentLessonDone ? 'Completed' : 'Mark as Completed'}
            </Button>
          </div>

          {/* Render by Lesson Type */}
          {activeLesson.lesson_type === 'video' && (
            <div className="aspect-video w-full rounded-2xl overflow-hidden bg-black border border-slate-800 shadow-2xl">
              <iframe
                src={activeLesson.video_url || 'https://www.youtube.com/embed/kqtD5dpn9C8'}
                title={activeLesson.title}
                className="w-full h-full"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowFullScreen
              />
            </div>
          )}

          {/* Interactive Coding Task Sandbox */}
          {activeLesson.lesson_type === 'coding_task' && activeLesson.coding_tasks && activeLesson.coding_tasks.length > 0 && (
            <div className="space-y-6">
              {activeLesson.coding_tasks.map((task) => (
                <div key={task.id} className="space-y-4">
                  {/* Task Instructions */}
                  <div className="p-5 rounded-2xl bg-slate-900/60 border border-slate-800 space-y-2">
                    <h3 className="text-sm font-bold text-white flex items-center gap-2">
                      <Terminal className="w-4 h-4 text-emerald-400" />
                      <span>{task.title}</span>
                    </h3>
                    <p className="text-xs text-slate-300 whitespace-pre-line leading-relaxed">{task.instructions}</p>
                    {task.hints && (
                      <p className="text-[11px] text-amber-400/90 pt-2 border-t border-slate-800">💡 Hint: {task.hints}</p>
                    )}
                  </div>

                  {/* Monaco / Code Runner Box */}
                  <div className="rounded-2xl border border-slate-800 bg-slate-900 overflow-hidden shadow-2xl">
                    <div className="bg-slate-950 px-4 py-2.5 border-b border-slate-800 flex items-center justify-between text-xs text-slate-400 font-mono">
                      <span>Python 3.12 Sandbox</span>
                      <Button
                        size="sm"
                        variant="primary"
                        onClick={() => handleRunCode(task.id)}
                        isLoading={isSubmittingCode}
                        leftIcon={<PlayCircle className="w-4 h-4" />}
                      >
                        Run & Test Code
                      </Button>
                    </div>
                    <textarea
                      value={userCode}
                      onChange={(e) => setUserCode(e.target.value)}
                      rows={10}
                      className="w-full bg-slate-900 p-4 font-mono text-xs text-slate-100 focus:outline-none resize-none leading-relaxed"
                      placeholder="Write your Python solution here..."
                      spellCheck={false}
                    />
                  </div>

                  {/* Task Output Panel */}
                  {taskResult && (
                    <div className={`p-4 rounded-xl border text-xs font-mono space-y-2 ${
                      taskResult.status === 'passed' ? 'bg-emerald-950/20 border-emerald-500/30 text-emerald-300' : 'bg-rose-950/20 border-rose-500/30 text-rose-300'
                    }`}>
                      <div className="flex items-center justify-between font-bold">
                        <span>Status: {taskResult.status.toUpperCase()}</span>
                        <span>{taskResult.passed_test_cases} / {taskResult.total_test_cases} Tests Passed</span>
                      </div>
                      <pre className="text-[11px] text-slate-300 whitespace-pre-wrap">{taskResult.output}</pre>
                      {taskResult.details && <p className="text-[11px] text-slate-400">{taskResult.details}</p>}
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}

          {/* Interactive Quiz Panel */}
          {activeLesson.lesson_type === 'quiz' && activeLesson.quizzes && activeLesson.quizzes.length > 0 && (
            <div className="space-y-6">
              {activeLesson.quizzes.map((quiz) => (
                <div key={quiz.id} className="p-6 rounded-2xl bg-slate-900 border border-slate-800 space-y-6">
                  <div className="space-y-1">
                    <h3 className="text-lg font-bold text-white">{quiz.title}</h3>
                    <p className="text-xs text-slate-400">Pass requirement: {quiz.pass_percentage}%</p>
                  </div>

                  <div className="space-y-6 divide-y divide-slate-800">
                    {quiz.questions.map((q, idx) => (
                      <div key={q.id} className="pt-4 space-y-3">
                        <p className="text-sm font-semibold text-slate-200">
                          {idx + 1}. {q.question_text}
                        </p>
                        <div className="space-y-2">
                          {q.options.map((opt) => {
                            const isSelected = (selectedAnswers[q.id] || []).includes(opt.id);
                            return (
                              <button
                                key={opt.id}
                                onClick={() => setSelectedAnswers({ ...selectedAnswers, [q.id]: [opt.id] })}
                                className={`w-full text-left p-3 rounded-xl border text-xs font-medium transition-all ${
                                  isSelected
                                    ? 'bg-brand-500/20 border-brand-500 text-brand-300'
                                    : 'bg-slate-950 border-slate-800 text-slate-300 hover:border-slate-700'
                                }`}
                              >
                                {opt.option_text}
                              </button>
                            );
                          })}
                        </div>
                      </div>
                    ))}
                  </div>

                  <Button
                    variant="primary"
                    className="w-full font-bold"
                    onClick={() => handleSubmitQuiz(quiz.id)}
                    isLoading={isSubmittingQuiz}
                  >
                    Submit Quiz Answers
                  </Button>

                  {/* Quiz Results */}
                  {quizResult && (
                    <div className={`p-4 rounded-xl border text-xs font-medium text-center space-y-1 ${
                      quizResult.passed ? 'bg-emerald-950/20 border-emerald-500/30 text-emerald-300' : 'bg-rose-950/20 border-rose-500/30 text-rose-300'
                    }`}>
                      <p className="text-sm font-bold">
                        {quizResult.passed ? '🎉 Congratulations! You Passed!' : '⚠️ Quiz Not Passed. Try Again!'}
                      </p>
                      <p>Your Score: {quizResult.score}% ({quizResult.correct_count} / {quizResult.total_questions} Correct)</p>
                    </div>
                  )}
                </div>
              ))}
            </div>
          )}

          {/* Lesson Article / Rich Notes */}
          {activeLesson.content && (
            <div className="p-6 rounded-2xl bg-slate-900/40 border border-slate-800 space-y-3">
              <h3 className="text-sm font-bold text-slate-200">Lesson Material</h3>
              <div className="prose prose-invert max-w-none text-xs text-slate-300 leading-relaxed whitespace-pre-line">
                {activeLesson.content}
              </div>
            </div>
          )}

          {/* Bottom Nav Buttons */}
          <div className="flex items-center justify-between pt-6 border-t border-slate-800/80 mt-auto">
            <Button
              variant="outline"
              size="sm"
              onClick={advanceToPrevLesson}
              leftIcon={<ChevronLeft className="w-4 h-4" />}
            >
              Previous Lesson
            </Button>
            <Button
              variant="primary"
              size="sm"
              onClick={advanceToNextLesson}
              rightIcon={<ChevronRight className="w-4 h-4" />}
            >
              Next Lesson
            </Button>
          </div>
        </div>

        {/* Right Sidebar: Curriculum Tree */}
        <aside className="w-full lg:w-80 border-t lg:border-t-0 lg:border-l border-slate-800 bg-slate-900/90 overflow-y-auto flex flex-col flex-shrink-0">
          <div className="p-4 border-b border-slate-800 font-bold text-xs text-slate-200 uppercase tracking-wider">
            Curriculum Modules
          </div>

          <div className="divide-y divide-slate-800">
            {curriculum.map((mod) => (
              <div key={mod.id} className="p-2 space-y-1">
                <div className="px-3 py-2 text-xs font-bold text-slate-300">
                  {mod.title}
                </div>
                <div className="space-y-0.5">
                  {mod.lessons.map((les) => {
                    const isDone = progress?.completed_lesson_ids.includes(les.id);
                    const isActive = activeLesson.id === les.id;
                    return (
                      <button
                        key={les.id}
                        onClick={() => selectLesson(les)}
                        className={`w-full text-left px-3 py-2 rounded-lg text-xs flex items-center justify-between transition-colors ${
                          isActive
                            ? 'bg-brand-500 text-white font-bold'
                            : 'text-slate-300 hover:bg-slate-800'
                        }`}
                      >
                        <div className="flex items-center gap-2 line-clamp-1">
                          {isDone ? (
                            <CheckCircle2 className={`w-3.5 h-3.5 flex-shrink-0 ${isActive ? 'text-white' : 'text-emerald-400'}`} />
                          ) : (
                            <Circle className="w-3.5 h-3.5 flex-shrink-0 text-slate-600" />
                          )}
                          <span className="truncate">{les.title}</span>
                        </div>
                        <span className={`text-[10px] flex-shrink-0 ml-2 ${isActive ? 'text-brand-100' : 'text-slate-500'}`}>
                          {les.duration_minutes}m
                        </span>
                      </button>
                    );
                  })}
                </div>
              </div>
            ))}
          </div>
        </aside>
      </div>

      {/* Certificate Modal */}
      <Modal
        isOpen={isCertModalOpen}
        onClose={() => setIsCertModalOpen(false)}
        title="Verified Certificate of Completion"
        maxWidth="4xl"
      >
        <div className="space-y-6 text-center">
          {certSvg ? (
            <div
              className="w-full rounded-2xl overflow-hidden shadow-2xl border border-slate-800"
              dangerouslySetInnerHTML={{ __html: certSvg }}
            />
          ) : (
            <div className="p-12 text-center text-slate-400">Loading certificate...</div>
          )}

          <div className="flex items-center justify-center gap-4">
            <Button
              variant="primary"
              onClick={() => {
                const blob = new Blob([certSvg || ''], { type: 'image/svg+xml' });
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `Certificate-${course?.title || 'CodePulse'}.svg`;
                a.click();
              }}
              leftIcon={<Download className="w-4 h-4" />}
            >
              Download SVG Certificate
            </Button>
          </div>
        </div>
      </Modal>
    </div>
  );
};
