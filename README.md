
Semantic Web Application Project


Overview

This project demonstrates two different approaches to building and querying semantic knowledge graphs, showcasing both traditional RDF-based methods and modern LLM-powered solutions.

Phase 1: Traditional Semantic Web Application

In the first phase, we implemented a semantic web application using Python with RDFLib. The application features:

Integration with Apache Jena Fuseki as the RDF store
A Flask-based web interface for querying the knowledge graph
SPARQL query support through a user-friendly web form
Structured display of query results

Technical Stack

Python (RDFLib) for RDF data manipulation
Apache Jena Fuseki for RDF storage
Flask for web application development
SPARQL for query processing

<img width="1227" alt="fuseki" src="https://github.com/user-attachments/assets/dcf0cf69-89a9-4e16-8fc6-c59e1918bb43" />

<img width="1528" alt="3030" src="https://github.com/user-attachments/assets/0589743a-e786-4024-a68f-af7688b61373" />

<img width="1523" alt="3030-info" src="https://github.com/user-attachments/assets/06f2a1f0-29fa-4c17-8f3d-a7e8609af0f7" />

Phase 2: Modern LLM-Based Approach

For those interested in a more modern approach, we've demonstrated an alternative method using:

Neo4J LLM Graph Builder
Natural Language Processing for query interpretation
Integration with advanced language models (e.g., Gemini 1.5 Flash)

This approach allows users to:

Convert ontology documents directly into knowledge graphs
Query the knowledge graph using natural language instead of SPARQL
Achieve similar functionality with reduced technical complexity

<img width="1526" alt="pahse2-gemini" src="https://github.com/user-attachments/assets/b67ac7f0-b6d3-4ac7-94b9-3a4cabe6d6dc" />

<img width="1443" alt="pahse2-graph" src="https://github.com/user-attachments/assets/f4aaca2b-2ecc-48b3-a056-639911eda390" />

<img width="1459" alt="q1" src="https://github.com/user-attachments/assets/c905d21b-45c7-4dbe-9b4e-515ba51cacd8" />

Advantages of Phase 2 Approach

Simplified graph creation from existing documentation
More intuitive querying through natural language
Reduced learning curve for non-technical users
Automated knowledge extraction and relationship mapping

Comparison

While Phase 1 demonstrates traditional semantic web technologies with precise control and structured querying, Phase 2 showcases how modern LLM-based tools can simplify both graph creation and querying processes. Users can choose the approach that best suits their technical requirements and expertise level.
Getting Started

For the traditional approach (Phase 1), follow the setup instructions in the main repository
For the LLM-based approach (Phase 2), refer to the Neo4J LLM Graph Builder documentation

Note to Users

If you find the traditional SPARQL querying approach challenging, consider exploring the Phase 2 implementation using Neo4J LLM Graph Builder. This alternative method allows for easier conversion of ontology documents into knowledge graphs and supports natural language queries, potentially offering a more accessible solution for your semantic web needs.


