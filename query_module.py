import json
import urllib.request


papers_example = [
    {
        'title': 'Jumping NLP Curves: A Review of Natural Language Processing Research',
        'abstract': 'Natural language processing (NLP) is a theory-motivated range of computational techniques for the automatic analysis and representation of human language. NLP research has evolved from the era of punch cards and batch processing (in which the analysis of a sentence could take up to 7 minutes) to the era of Google and the likes of it (in which millions of webpages can be processed in less than a second). This review paper draws on recent developments in NLP research to look at the past, present, and future of NLP technology in a new light. Borrowing the paradigm of jumping curves from the field of business management and marketing prediction, this survey article reinterprets the evolution of NLP research as the intersection of three overlapping curves-namely Syntactics, Semantics, and Pragmatics Curveswhich will eventually lead NLP research to evolve into natural language understanding.',
        'venue': 'IEEE Computational intelligence ',
        'authors': ['E Cambria', 'B White'],
        'year': 2014,
        'n_citations': 900,
    },
    {
        'title': 'BERT rediscovers the classical NLP pipeline',
        'abstract': 'Pre-trained text encoders have rapidly advanced the state of the art on many NLP tasks. We focus on one such model, BERT, and aim to quantify where linguistic information is captured within the network. We find that the model represents the steps of the traditional NLP pipeline in an interpretable and localizable way, and that the regions responsible for each step appear in the expected sequence: POS tagging, parsing, NER, semantic roles, then coreference. Qualitative analysis reveals that the model can and often does adjust this pipeline dynamically, revising lower-level decisions on the basis of disambiguating information from higher-level representations.',
        'venue': 'Computation and Language',
        'authors': ['Ian Tenney', 'Dipanjan Das', 'Ellie Pavlick'],
        'year': 2015,
        'n_citations': 519  # we don't have n_key_citations here and that's OK
    },
    {
        'title': 'Neural networks in civil engineering. I: Principles and understanding',
        'abstract': 'This is the first of two papers providing a discourse on the understanding, usage, and potential for application of artificial neural networks within civil engineering.',
        'venue': 'Journal of computing in civil engineering',
        'authors': ['Ian Flood', 'Nabil Kartam'],
        'year': 1994,
        'n_citations': 810  # we don't have n_key_citations here and that's OK
    },
    {
        'title': 'Xlnet: Generalized autoregressive pretraining for language understanding',
        'abstract': 'With the capability of modeling bidirectional contexts, denoising autoencoding based pretraining like BERT achieves better performance than pretraining approaches based on autoregressive language modeling.',
        'venue': 'Advances in neural networks',
        'authors': ['Z Yang', 'Z Dai'],
        'year': 2019,
        'n_citations': 3581  # we don't have n_key_citations here and that's OK
    }
]

def query_from_API(keywords, numbers):
    query_url = 'https://api.semanticscholar.org/graph/v1/paper/search?query=' + keywords + '&fields=title,abstract,venue,authors,year,citationCount&limit=' + numbers

    with urllib.request.urlopen(query_url) as url:
        s = url.read()

    s = json.loads(s)

    paper_dict_list = []

    for i in range(len(s['data'])):
        # paper_dict_format[i]['title'] = s['data'][i]['title']
        author_list = []
        for author in range(len(s['data'][i]['authors'])):
            author_list.append(s['data'][i]['authors'][author]['name'])

        new_paper = {'title': s['data'][i]['title'], 'abstract': s['data'][i]['abstract'],
                     'venue': s['data'][i]['venue'], 'authors': author_list, 'year': s['data'][i]['year'],
                     'n_citations': s['data'][i]['citationCount']}
        paper_dict_list.append(new_paper)

    return paper_dict_list

def reorder_bycitations(paper_list):
    cite_order = []
    for paper in paper_list:
        cite_order.append(int(paper['n_citations']))
    cite_order = sorted(range(len(cite_order)), key=lambda k: cite_order[k], reverse=True)
    paper_list = [paper_list[i] for i in cite_order]

    return paper_list


def reorder_bydate(paper_list):
    date_order = []
    for paper in paper_list:
        date_order.append(int(paper['year']))
    print(date_order)
    date_order = sorted(range(len(date_order)), key=lambda k: date_order[k], reverse=True)
    paper_list = [paper_list[i] for i in date_order]
    return paper_list

def reorder_byML(paper_list):
    return paper_list
