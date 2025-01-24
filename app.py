from flask import Flask, render_template, request, redirect, url_for
from rdflib import Graph
from rdflib.plugins.stores import sparqlstore
from queries import QUERIES

app = Flask(__name__)

def get_store():
    store = sparqlstore.SPARQLUpdateStore()
    store.open(("http://localhost:3030/film-ontology/query",
                "http://localhost:3030/film-ontology/update"))
    return store

def init_graph():
    store = get_store()
    return Graph(store)

@app.route('/')
def index():
    return render_template('index.html', queries=QUERIES)

@app.route('/query', methods=['POST'])
def query():
    selected_query = request.form.get('query_select')
    custom_query = request.form.get('custom_query')
    query = custom_query if custom_query else QUERIES.get(selected_query, QUERIES['query1'])

    try:
        g = init_graph()
        results = g.query(query)

        processed_results = []
        headers = results.vars

        for row in results:
            processed_results.append([str(cell) for cell in row])

        return render_template('results.html',
                               results=processed_results,
                               headers=headers,
                               query=query)

    except Exception as e:
        return render_template('index.html',
                               error=f"Query error: {str(e)}",
                               queries=QUERIES)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5001, use_reloader=True)