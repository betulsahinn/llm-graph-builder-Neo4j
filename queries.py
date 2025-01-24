QUERIES = {
    'query1': """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX film: <http://www.semanticweb.org/film-ontology#>

    SELECT ?filmTitle ?year
    WHERE {
        ?film film:hasDirector film:ChristopherNolan ;
              film:title ?filmTitle ;
              film:releaseYear ?year .
    }
    ORDER BY ?year
    """,

    'query2': """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX film: <http://www.semanticweb.org/film-ontology#>

    SELECT ?actorName ?filmTitle
    WHERE {
        ?film film:hasActor ?actor ;
              film:title ?filmTitle .
        ?actor film:name ?actorName .
        FILTER(?actorName = "Leonardo DiCaprio")
    }
    """,

    'query3': """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX film: <http://www.semanticweb.org/film-ontology#>

    SELECT ?filmTitle ?genreName
    WHERE {
        ?film film:hasGenre ?genre ;
              film:title ?filmTitle .
        ?genre film:name ?genreName .
        FILTER(?genreName = "Action")
    }
    """
}