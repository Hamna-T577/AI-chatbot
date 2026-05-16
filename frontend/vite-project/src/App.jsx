import { useState, useRef, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const chatEndRef = useRef(null);

  // auto scroll
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const handleUpload = async () => {
    if (!file) return alert("Please select a file");

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);

      const response = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData
      );

      setMessages((prev) => [
        ...prev,
        { type: "bot", text: "📄 Document uploaded successfully!" },
      ]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { type: "bot", text: "Upload failed ❌" },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const askQuestion = async () => {
    if (!question.trim()) return;

    const userMsg = { type: "user", text: question };
    setMessages((prev) => [...prev, userMsg]);

    setQuestion("");
    setLoading(true);

    try {
      const res = await axios.post(
        `http://127.0.0.1:8000/chat?query=${question}`
      );

      const botMsg = { type: "bot", text: res.data.answer };

      setMessages((prev) => [...prev, botMsg]);
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        { type: "bot", text: "⚠️ Error getting response" },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      {/* HEADER */}
      <header className="header">
        <h1>AI Document Chat</h1>
        <p>Upload a document and ask anything about it</p>
      </header>

      {/* UPLOAD CARD */}
      <div className="uploadCard">
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button onClick={handleUpload}>Upload</button>
      </div>

      {/* CHAT BOX */}
      <div className="chatContainer">
        <div className="messages">
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`msg ${msg.type === "user" ? "user" : "bot"}`}
            >
              {msg.text}
            </div>
          ))}

          {loading && <div className="typing">Thinking...</div>}

          <div ref={chatEndRef} />
        </div>

        {/* INPUT AREA */}
        <div className="inputBox">
          <input
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="Ask anything about your document..."
            onKeyDown={(e) => e.key === "Enter" && askQuestion()}
          />

          <button onClick={askQuestion}>Send</button>
        </div>
      </div>
    </div>
  );
}

export default App;