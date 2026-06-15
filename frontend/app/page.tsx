"use client";
import { useState } from "react";
import { generateComic } from "@/lib/api";

export default function Home() {
  
  const [prompt, setPrompt] = useState("");
  const [style, setStyle] = useState("Comic");
  const [panelCount, setPanelCount] = useState(4);
  const [loading, setLoading] = useState(false);
  const [status, setStatus] = useState("");
  type ComicResponse = {
    title: string;
    character: string;
    comic_url: string;
  };

  const [comic, setComic] =
    useState<ComicResponse | null>(null);

  async function handleGenerate() {

    if (!prompt.trim()) {
      alert("Please enter a prompt");
      return;
    }

    try {

      setLoading(true);
      setStatus("Generating Story...");
      setStatus(
        "Generating Images..."
      );
      const data = await generateComic(
        prompt,
        panelCount,
        style
      );

      setComic(data);
      setStatus("Done");

    } catch (error) {

      console.error(error);

      alert(
        "Comic generation failed. Please try again."
      );

    } finally {

      setLoading(false);

    }
  }

  return (
    <main className="min-h-screen px-6 py-8">

      <div className="mx-auto max-w-7xl">

        {/* Navbar */}

        <nav className="mb-12 flex items-center justify-between">

          <h1 className="text-2xl font-bold text-white">
            ComicCrafter AI
          </h1>

          <div className="hidden gap-8 text-zinc-400 md:flex">
            <a href="#">Features</a>
            <a href="#">Generate</a>
            <a href="#">About</a>
          </div>

          <a
            href="#"
            className="
              rounded-xl
              border
              border-white/10
              bg-white/5
              px-4
              py-2
              text-sm
              text-white
              backdrop-blur-xl
            "
          >
            GitHub
          </a>

        </nav>

        {/* Hero */}

        <section className="mb-12 text-center">

          <div className="inline-flex items-center rounded-full border border-white/10 bg-white/5 px-4 py-2 text-sm text-zinc-300 backdrop-blur-xl">
            ✨ AI-Powered Comic Generation
          </div>

          <h1 className="mt-6 text-5xl font-bold text-white md:text-6xl">
            Transform Ideas Into Comics
          </h1>

          <p className="mx-auto mt-4 max-w-2xl text-zinc-400 text-lg">
            Generate AI-powered stories, comic panels and complete comic
            pages in seconds.
          </p>

        </section>

        {/* Main Workspace */}

        <section className="grid gap-8 lg:grid-cols-2">

          {/* Left Panel */}

          <div
            className="
              rounded-3xl
              border
              border-white/10
              bg-white/5
              p-8
              backdrop-blur-xl
            "
          >

            <h2 className="mb-6 text-2xl font-semibold text-white">
              Generate Comic
            </h2>

            <textarea
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Describe your comic idea..."
              className="
                h-52
                w-full
                resize-none
                rounded-2xl
                border
                border-white/10
                bg-black/30
                p-4
                text-white
                outline-none
              "
            />

            <div className="mt-6 grid gap-4 md:grid-cols-2">

              <div>
                <label className="mb-2 block text-zinc-300">
                  Style
                </label>

                <select
                  value={style}
                  onChange={(e) =>
                    setStyle(e.target.value)
                  }
                  className="
                    w-full
                    rounded-xl
                    border
                    border-white/10
                    bg-black/30
                    p-3
                    text-white
                  "
                >
                  <option>Comic</option>
                  <option>Manga</option>
                  <option>Webtoon</option>
                </select>
              </div>

              <div>
                <label className="mb-2 block text-zinc-300">
                  Panels
                </label>

                <select
                  value={panelCount}
                  onChange={(e) =>
                    setPanelCount(
                      Number(e.target.value)
                    )
                  }
                  className="
                    w-full
                    rounded-xl
                    border
                    border-white/10
                    bg-black/30
                    p-3
                    text-white
                  "
                >
                  <option value={4}>4</option>
                  <option value={6}>6</option>
                  <option value={8}>8</option>
                </select>
              </div>

            </div>

            <button
              onClick={handleGenerate}
              disabled={loading}
              className="
                mt-8
                w-full
                rounded-2xl
                bg-gradient-to-r
                from-blue-600
                to-purple-600
                py-4
                text-lg
                font-semibold
                text-white
                transition
                hover:scale-[1.01]
                disabled:opacity-60
              "
            >
              {loading
                ? status
                : "✨ Generate Comic"}
            </button>

          </div>

          {/* Right Panel */}

          <div
            className="
              rounded-3xl
              border
              border-white/10
              bg-white/5
              p-8
              backdrop-blur-xl
            "
          >

            <div className="flex items-center justify-between">

              <h2 className="text-2xl font-semibold text-white">
                Live Preview
              </h2>

              <span className="text-sm text-zinc-500">
                {loading ? "Generating..." : "Ready"}
              </span>

            </div>

            <div
              className="
                mt-6
                h-[500px]
                overflow-y-auto
                rounded-2xl
                border
                border-dashed
                border-white/10
                bg-black/20
                p-6
              "
            >

              {comic ? (

                <div className="space-y-4">

                  <h3 className="text-2xl font-bold text-white">
                    {comic.title}
                  </h3>

                  <img
                    src={comic.comic_url}
                    alt={comic.title}
                    className="
                      w-full
                      rounded-xl
                      border
                      border-white/10
                      object-contain
                    "
                  />

                  <a
                    href={comic.comic_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="
                      inline-block
                      rounded-xl
                      bg-gradient-to-r
                      from-blue-600
                      to-purple-600
                      px-5
                      py-3
                      text-white
                      font-semibold
                    "
                  >
                    Download Comic
                  </a>

                </div>

              ) : (

                <div className="flex h-full items-center justify-center">

                  <div className="text-center">

                    <div className="mb-4 text-6xl">
                      🖼️
                    </div>

                    <h3 className="text-xl font-semibold text-white">
                      No Comic Generated Yet
                    </h3>

                    <p className="mt-2 text-zinc-400">
                      Your generated comic pages will
                      appear here.
                    </p>

                  </div>

                </div>

              )}

            </div>

          </div>

        </section>

        {/* Stats */}

        <section className="mt-12 grid gap-6 md:grid-cols-3">

          <div className="rounded-2xl border border-white/10 bg-white/5 p-6 text-center backdrop-blur-xl">
            <h3 className="text-3xl font-bold text-white">4-8</h3>
            <p className="mt-2 text-zinc-400">Panel Support</p>
          </div>

          <div className="rounded-2xl border border-white/10 bg-white/5 p-6 text-center backdrop-blur-xl">
            <h3 className="text-3xl font-bold text-white">AI</h3>
            <p className="mt-2 text-zinc-400">Story Generation</p>
          </div>

          <div className="rounded-2xl border border-white/10 bg-white/5 p-6 text-center backdrop-blur-xl">
            <h3 className="text-3xl font-bold text-white">Fast</h3>
            <p className="mt-2 text-zinc-400">Comic Creation</p>
          </div>

        </section>

      </div>

    </main>
  );
}