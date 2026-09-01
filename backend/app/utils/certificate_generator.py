import html


def generate_certificate_svg(
    student_name: str,
    course_title: str,
    instructor_name: str,
    cert_code: str,
    issue_date: str,
    grade: float = 100.0
) -> str:
    """Generate professional vector SVG certificate markup."""
    safe_student = html.escape(student_name)
    safe_course = html.escape(course_title)
    safe_instructor = html.escape(instructor_name)
    safe_code = html.escape(cert_code)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 700" width="1000" height="700">
  <defs>
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="50%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#090d16" />
    </linearGradient>
    <linearGradient id="gold-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fbbf24" />
      <stop offset="50%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#d97706" />
    </linearGradient>
    <linearGradient id="blue-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#6366f1" />
    </linearGradient>
    <filter id="shadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="1000" height="700" fill="url(#bg-grad)" rx="16"/>

  <!-- Ornate Border -->
  <rect x="30" y="30" width="940" height="640" fill="none" stroke="url(#gold-grad)" stroke-width="2" stroke-dasharray="8 4" rx="12"/>
  <rect x="45" y="45" width="910" height="610" fill="none" stroke="#334155" stroke-width="1" rx="8"/>

  <!-- Header Badge -->
  <circle cx="500" cy="110" r="36" fill="#1e293b" stroke="url(#gold-grad)" stroke-width="3" filter="url(#shadow)"/>
  <path d="M485 110 L495 120 L515 98" fill="none" stroke="url(#gold-grad)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>

  <!-- Platform Brand -->
  <text x="500" y="175" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="16" font-weight="700" fill="#94a3b8" letter-spacing="4">CODEPULSE ACADEMY</text>
  <text x="500" y="215" text-anchor="middle" font-family="'Georgia', serif" font-size="34" font-weight="bold" fill="url(#gold-grad)" letter-spacing="2">CERTIFICATE OF COMPLETION</text>

  <!-- Subtitle -->
  <text x="500" y="250" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="15" fill="#cbd5e1">This is proudly presented to</text>

  <!-- Student Name -->
  <text x="500" y="310" text-anchor="middle" font-family="'Georgia', serif" font-size="40" font-weight="bold" fill="#ffffff" filter="url(#shadow)">{safe_student}</text>
  <line x1="280" y1="330" x2="720" y2="330" stroke="url(#blue-grad)" stroke-width="2"/>

  <!-- Description -->
  <text x="500" y="375" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="16" fill="#94a3b8">for successfully demonstrating mastery and completing all requirements for the professional course</text>

  <!-- Course Title -->
  <text x="500" y="425" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="28" font-weight="bold" fill="url(#blue-grad)">{safe_course}</text>

  <!-- Grade Badge -->
  <rect x="425" y="450" width="150" height="30" rx="15" fill="#1e293b" stroke="#38bdf8" stroke-width="1"/>
  <text x="500" y="470" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="13" font-weight="600" fill="#38bdf8">Final Score: {grade:.0f}%</text>

  <!-- Signatures & Verification -->
  <g transform="translate(120, 520)">
    <!-- Instructor Sign -->
    <line x1="0" y1="60" x2="220" y2="60" stroke="#475569" stroke-width="1"/>
    <text x="110" y="50" text-anchor="middle" font-family="'Brush Script MT', cursive, serif" font-size="24" fill="#f8fafc">{safe_instructor}</text>
    <text x="110" y="80" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="13" font-weight="600" fill="#cbd5e1">Lead Instructor</text>
    <text x="110" y="98" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="11" fill="#64748b">CodePulse Academy</text>
  </g>

  <g transform="translate(660, 520)">
    <!-- Issue Date & Verification -->
    <line x1="0" y1="60" x2="220" y2="60" stroke="#475569" stroke-width="1"/>
    <text x="110" y="50" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="16" font-weight="bold" fill="#f8fafc">{issue_date}</text>
    <text x="110" y="80" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="13" font-weight="600" fill="#cbd5e1">Date of Issuance</text>
    <text x="110" y="98" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="11" fill="#64748b">ID: {safe_code}</text>
  </g>

  <!-- Verified Seal in Center -->
  <g transform="translate(450, 530)">
    <circle cx="50" cy="50" r="40" fill="#0f172a" stroke="url(#gold-grad)" stroke-width="2"/>
    <circle cx="50" cy="50" r="32" fill="none" stroke="#f59e0b" stroke-width="1" stroke-dasharray="4 2"/>
    <text x="50" y="46" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="9" font-weight="bold" fill="#fbbf24">VERIFIED</text>
    <text x="50" y="58" text-anchor="middle" font-family="'Segoe UI', system-ui, sans-serif" font-size="8" fill="#e2e8f0">GENUINE</text>
  </g>
</svg>"""
