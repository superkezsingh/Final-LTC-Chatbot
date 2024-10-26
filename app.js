const { Configuration, OpenAIApi } = require("openai");
require("dotenv").config();

const configuration = new Configuration({
  apiKey: process.env.OPENAI_API_KEY,
});
const openai = new OpenAIApi(configuration);

const express = require("express");
const app = express();
app.use(express.json());

app.post("/chat", async (req, res) => {
  try {
    const { message } = req.body;
    const response = await openai.createChatCompletion({
      model: "gpt-3.5-turbo",
      messages: [{ role: "user", content: message }],
    });
    res.json({ response: response.data.choices[0].message.content });
  } catch (error) {
    console.error(error);
    res.status(500).send("An error occurred");
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
