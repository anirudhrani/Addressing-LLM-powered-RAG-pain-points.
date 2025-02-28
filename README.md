# Addressing the Challenges of LLM-Powered Retrieval-Augmented Generation

This project, developed for our Spring 2024 course, investigates how we can enhance large language models by integrating external knowledge through a Retrieval-Augmented Generation (RAG) framework. We explore and address common challenges in RAG systems, such as missing content, retrieval inaccuracies, improper document merging, flawed information extraction, formatting issues, specificity problems, and partial responses.

## Experimental Setup

To rigorously evaluate our RAG framework, we designed a series of experiments focusing on several critical aspects of the system:

- **Content Completeness:**  
  We compared outputs using a baseline prompt against those generated with an improved prompt strategy. Our experiments demonstrated that refining the prompt can significantly reduce hallucination levels, ensuring that the model produces complete and accurate responses.

- **Retrieval Accuracy:**  
  We examined the efficiency of our retrieval component by contrasting baseline retrieval methods with our advanced techniques. Our evaluation measured how well the system incorporates relevant information into the final context, leading to substantial improvements in output quality.

- **Document Merging and Information Extraction:**  
  By experimenting with different text chunk sizes (256, 512, and 1024 tokens) and varying the number of top documents retrieved (Top-K), we were able to balance retrieval efficiency with the need for detailed and contextually appropriate responses.

- **Format Handling and Specificity:**  
  We analyzed how different data formats—such as tables, lists, and prose—affect the model’s ability to maintain the correct level of detail. Our experiments allowed us to fine-tune the system so that it consistently delivers outputs with the appropriate specificity.

- **Mitigating Partial Responses:**  
  Through a systematic evaluation of our document merging techniques and retrieval processes, we identified and addressed scenarios where the model generated incomplete answers, ensuring a comprehensive synthesis of the available information.

## Dataset

For our experiments, we curated a comprehensive dataset comprising academic research papers, articles, and other relevant documents in the field of large language models and retrieval-augmented generation. Key aspects of our dataset include:

- **Document Collection and Preprocessing:**  
  We gathered a diverse range of documents that cover both foundational concepts and cutting-edge research in LLMs and RAG systems. Each document was segmented into manageable text chunks, which were then converted into numerical embeddings that capture their semantic meaning.

- **Vector Database Indexing:**  
  The generated embeddings were indexed in a vector database. This setup allowed us to efficiently retrieve contextually relevant passages when a prompt was given, ensuring that the model has access to the most pertinent information during the generation process.

- **Evaluation:**  
  The dataset was instrumental in our experimental evaluations, enabling us to test various retrieval strategies, prompt refinements, and document merging techniques. By systematically varying the dataset parameters (such as chunk size and retrieval scope), we could assess the impact on overall system performance and fine-tune our RAG framework accordingly.
