# 🎭 ComicCrafter AI

ComicCrafter AI is an AI-powered comic generator that creates **short comic-style stories** with AI-generated images. The app runs **locally on edge devices** and uses **OpenAI's GPT-4o** for story generation and **Stability AI** for image generation.

## 🚀 Features

- **AI Story Generation**: Uses OpenAI's GPT-4o to generate a four-panel story.
- **AI Image Generation**: Uses Stability AI to generate matching images.
- **Seamless UI**: Built with Streamlit for an easy-to-use interface.
- **Edge Deployment**: Optimized for running on local devices.

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python
- **LLM**: OpenAI GPT-4o
- **Image Generation**: Stability AI API
- **Environment Management**: Dotenv

## 📦 Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/your-username/ComicCrafterAI.git
   cd ComicCrafterAI
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the project root and add:

   ```sh
   OPENAI_API_KEY=your-openai-api-key
   STABILITY_API_KEY=your-stability-ai-key
   ```

## 🎮 Usage

Run the Streamlit app:

```sh
streamlit run app.py
```

Then open the browser at `http://localhost:8501/` to interact with the app.

## 📝 Roadmap

- ✅ Basic story and image generation
- ⏳ Multi-panel comic book mode
- ⏳ Local model deployment for offline use
- ⏳ Custom styling for comic panels

## 🤝 Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

.

