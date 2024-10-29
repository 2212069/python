𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 𝐚𝐧𝐝 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬

𝐐𝐮𝐞𝐬𝐭𝐢𝐨𝐧-𝐀𝐧𝐬𝐰𝐞𝐫𝐢𝐧𝐠 𝐅𝐮𝐧𝐜𝐭𝐢𝐨𝐧𝐚𝐥𝐢𝐭𝐲:

     The app uses a distilbert-base-uncased-distilled-squad model for answering fact-based questions. Users type a question about Albert Einstein, and the model retrieves the most relevant answer from the context.
𝐒𝐮𝐦𝐦𝐚𝐫𝐢𝐳𝐚𝐭𝐢𝐨𝐧 𝐅𝐞𝐚𝐭𝐮𝐫𝐞:
     For summarizing, the app uses the facebook/bart-large-cnn model to condense the provided Einstein-related content. Users can click the "Summarize Context" button to generate a brief summary.
Interactive and User-Friendly Design:

    The interface is designed with Gradio’s Blocks, providing a structured layout and colorful custom buttons. The main title and subtitle are styled with color for visual appeal.
The app includes two primary buttons with different colors: a green button for question-answering and an orange button for summarization.

𝐔𝐈 𝐂𝐨𝐦𝐩𝐨𝐧𝐞𝐧𝐭𝐬:
   Text boxes for user input (question) and model output (answer and summary) with clear labels and placeholders make it intuitive to use.
The app features responsive elements: typing a question or clicking a button triggers the associated model.

𝐖𝐨𝐫𝐤𝐢𝐧𝐠 𝐏𝐫𝐢𝐧𝐜𝐢𝐩𝐥𝐞
   Loading Models: The question-answering and summarization pipelines are initialized with pre-trained models, preparing them to process inputs as soon as the app runs.
Question Submission:
    When a user submits a question, it passes through the answer_factoid_question function, which invokes the QA model on the context. The answer is extracted and displayed in the “Answer” textbox.
Summarization Trigger:
     Clicking "Summarize Context" calls the summarize_text function, passing the context into the summarization pipeline. The generated summary appears in the "Summary" textbox.





