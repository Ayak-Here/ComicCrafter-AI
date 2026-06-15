const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL!;

export async function generateStory(
  prompt: string,
  panelCount: number
) {

  const response = await fetch(
    `${API_BASE_URL}/generate-story`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        prompt,
        panel_count: panelCount,
      }),
    }
  );

  if (!response.ok) {
    throw new Error("Failed to generate story");
  }

  return response.json();
}

export async function generateComic(
  prompt: string,
  panelCount: number,
  style: string
) {

  const response = await fetch(
    `${API_BASE_URL}/generate-comic`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        prompt,
        panel_count: panelCount,
        style,
      }),
    }
  );

  if (!response.ok) {
    throw new Error(
      "Failed to generate comic"
    );
  }

  return response.json();
}