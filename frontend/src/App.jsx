
function App() {
  return (
    <div className="min-h-screen bg-[#070b14] text-white">
      {/* Navigation */}
      <nav className="flex items-center justify-between border-b border-white/10 px-6 py-5 md:px-16">
        <h1 className="text-2xl font-bold tracking-wide">
          Sentinel<span className="text-emerald-400">AI</span>
        </h1>

        <div className="hidden items-center gap-8 text-sm text-slate-300 md:flex">
          <a href="#features" className="hover:text-emerald-400">
            Features
          </a>
          <a href="#about" className="hover:text-emerald-400">
            About
          </a>
        </div>

        <a
          href="#features"
          className="rounded-lg border border-emerald-400/40 px-4 py-2 text-sm text-emerald-300 transition hover:bg-emerald-400/10"
        >
          Explore Platform
        </a>
      </nav>

      {/* Hero section */}
      <main className="mx-auto flex max-w-7xl flex-col items-center px-6 py-24 text-center md:py-32">
        <div className="mb-8 rounded-full border border-emerald-400/20 bg-emerald-400/10 px-4 py-2 text-sm text-emerald-300">
          Intelligent Security Monitoring
        </div>

        <h2 className="max-w-4xl text-4xl font-bold leading-tight tracking-tight sm:text-5xl md:text-7xl">
          Detect threats.
          <br />
          <span className="text-emerald-400">
            Protect what matters.
          </span>
        </h2>

        <p className="mt-7 max-w-2xl text-base leading-8 text-slate-400 md:text-lg">
          Analyze security logs, uncover suspicious login activity,
          and investigate potential threats with rule-based detection
          and locally trained machine learning.
        </p>

        <div className="mt-10 flex flex-col gap-4 sm:flex-row">
          <a
            href="#features"
            className="rounded-lg bg-emerald-400 px-7 py-3.5 font-semibold text-slate-950 transition hover:bg-emerald-300"
          >
            Explore Features →
          </a>

          <a
            href="#about"
            className="rounded-lg border border-white/15 px-7 py-3.5 font-semibold text-white transition hover:bg-white/5"
          >
            Learn About SentinelAI
          </a>
        </div>

        
        {/* Dashboard Preview */}
        <section className="mt-20 w-full max-w-5xl rounded-2xl border border-white/10 bg-[#0c1220] p-5 text-left shadow-2xl shadow-emerald-950/20 md:p-8">
          <div className="flex flex-col justify-between gap-4 sm:flex-row sm:items-center">
            <div>
              <p className="text-sm text-slate-400">SENTINELAI / OVERVIEW</p>
              <h3 className="mt-2 text-xl font-semibold">
                Security Operations
              </h3>
            </div>

            <div className="flex items-center gap-2 text-sm text-amber-300">
              <span className="h-2 w-2 rounded-full bg-amber-400" />
              Demo preview
            </div>
          </div>

          <div className="mt-7 grid grid-cols-1 gap-4 sm:grid-cols-3">
            <div className="rounded-xl border border-white/10 bg-white/[0.03] p-5">
              <p className="text-sm text-slate-400">Events analyzed</p>
              <p className="mt-3 text-3xl font-bold">2,481</p>
              <p className="mt-2 text-xs text-slate-500">Illustrative data</p>
            </div>

            <div className="rounded-xl border border-white/10 bg-white/[0.03] p-5">
              <p className="text-sm text-slate-400">Alerts generated</p>
              <p className="mt-3 text-3xl font-bold text-amber-300">18</p>
              <p className="mt-2 text-xs text-slate-500">Illustrative data</p>
            </div>

            <div className="rounded-xl border border-white/10 bg-white/[0.03] p-5">
              <p className="text-sm text-slate-400">High priority</p>
              <p className="mt-3 text-3xl font-bold text-rose-400">4</p>
              <p className="mt-2 text-xs text-slate-500">Requires review</p>
            </div>
          </div>

          
          {/* Illustrative activity visualization */}
          <div className="mt-6 rounded-xl border border-white/10 bg-white/[0.02] p-5">
            <div className="flex flex-col justify-between gap-2 sm:flex-row sm:items-center">
              <div>
                <h4 className="font-semibold">Login activity</h4>
                <p className="mt-1 text-sm text-slate-500">
                  Illustrative event volume
                </p>
              </div>
              <span className="text-xs text-slate-500">
                Demo data · Not live monitoring
              </span>
            </div>

            <div className="mt-6 flex h-40 items-end gap-3">
              {[
                { label: "Mon", height: "35%" },
                { label: "Tue", height: "55%" },
                { label: "Wed", height: "42%" },
                { label: "Thu", height: "78%" },
                { label: "Fri", height: "60%" },
                { label: "Sat", height: "92%" },
                { label: "Sun", height: "48%" },
              ].map((day) => (
                <div
                  key={day.label}
                  className="flex h-full flex-1 flex-col items-center justify-end gap-3"
                >
                  <div
                    className="w-full max-w-12 rounded-t-md bg-emerald-400/70 transition hover:bg-emerald-300"
                    style={{ height: day.height }}
                    title={`${day.label}: illustrative activity`}
                  />
                  <span className="text-xs text-slate-500">
                    {day.label}
                  </span>
                </div>
              ))}
            </div>
          </div>


          <div className="mt-6 overflow-hidden rounded-xl border border-white/10">
            <div className="border-b border-white/10 px-5 py-4">
              <h4 className="font-semibold">Recent activity</h4>
            </div>

            <div className="divide-y divide-white/10">
              <div className="flex flex-col justify-between gap-2 px-5 py-4 sm:flex-row sm:items-center">
                <div>
                  <p className="font-medium">Repeated login failures</p>
                  <p className="mt-1 text-sm text-slate-500">
                    Source: 192.0.2.24
                  </p>
                </div>
                <span className="w-fit rounded-full bg-rose-400/10 px-3 py-1 text-xs text-rose-300">
                  High
                </span>
              </div>

              <div className="flex flex-col justify-between gap-2 px-5 py-4 sm:flex-row sm:items-center">
                <div>
                  <p className="font-medium">Unusual login timing</p>
                  <p className="mt-1 text-sm text-slate-500">
                    Source: 198.51.100.18
                  </p>
                </div>
                <span className="w-fit rounded-full bg-amber-400/10 px-3 py-1 text-xs text-amber-300">
                  Medium
                </span>
              </div>

              <div className="flex flex-col justify-between gap-2 px-5 py-4 sm:flex-row sm:items-center">
                <div>
                  <p className="font-medium">Multiple accounts attempted</p>
                  <p className="mt-1 text-sm text-slate-500">
                    Source: 203.0.113.42
                  </p>
                </div>
                <span className="w-fit rounded-full bg-rose-400/10 px-3 py-1 text-xs text-rose-300">
                  High
                </span>
              </div>
            </div>
          </div>
        </section>


        {/* Feature highlights */}
        <section
          id="features"
          className="mt-24 grid w-full max-w-5xl grid-cols-1 gap-5 text-left sm:grid-cols-3"
        >
          <div className="rounded-xl border border-white/10 bg-white/[0.03] p-6">
            <div className="mb-4 text-2xl">⌘</div>
            <h3 className="text-lg font-semibold">Log Analysis</h3>
            <p className="mt-2 text-sm leading-6 text-slate-400">
              Import authentication logs and explore security events.
            </p>
          </div>

          <div className="rounded-xl border border-white/10 bg-white/[0.03] p-6">
            <div className="mb-4 text-2xl text-emerald-400">⌁</div>
            <h3 className="text-lg font-semibold">Threat Detection</h3>
            <p className="mt-2 text-sm leading-6 text-slate-400">
              Identify suspicious patterns using transparent rules
              and anomaly detection.
            </p>
          </div>

          <div className="rounded-xl border border-white/10 bg-white/[0.03] p-6">
            <div className="mb-4 text-2xl">◷</div>
            <h3 className="text-lg font-semibold">Incident Tracking</h3>
            <p className="mt-2 text-sm leading-6 text-slate-400">
              Review alerts and track investigations in one place.
            </p>
          </div>
        </section>

        {/* About section */}
        <section id="about" className="mt-24 max-w-3xl">
          <h3 className="text-2xl font-bold md:text-3xl">
            Security insights, made actionable.
          </h3>
          <p className="mt-5 leading-8 text-slate-400">
            SentinelAI combines understandable detection rules with
            machine learning to help security analysts prioritize
            unusual authentication activity. An alert is a signal
            for investigation, not proof of an attack.
          </p>
        </section>
      </main>

      {/* Footer */}
      <footer className="border-t border-white/10 px-6 py-6 text-center text-sm text-slate-500">
        SentinelAI · Intelligent Threat Detection Dashboard
      </footer>
    </div>
  );
}

export default App;
