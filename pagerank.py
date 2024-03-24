import os
import random
import re
import sys
import math
import copy

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    N = len(corpus)

    # if page has no outgoing links
    if not corpus[page]:
        pages_dict = {}
        for p in corpus:
            pages_dict[p] = 1 / N
    else:
        # create a list and a dict with all pages that the current page might link to
        pages_dict = {}
        pages_list = []
        for p in corpus[page]:
            pages_dict[p] = 0
            pages_list.append(p)
        
        for link in pages_list:
            pages_dict[link] = damping_factor * (1 / len(pages_list))

        # adding (1-d) / N back in
        for link in pages_list:
            pages_dict[link] += (1 - damping_factor) * (1 / N)
        
        # considering possibility of jumping to links not in pages_link
        for p in corpus:
            if p not in pages_dict:
                pages_dict[p] = (1 - damping_factor) * (1 / N)

    # check if the probability distrubution sum to 1
    Sum = sum(list(pages_dict.values()))
    if math.isclose(Sum, 1, rel_tol=1e-9):
        return pages_dict
    else:
        raise ValueError(f"Error in transition_model. Wrong sum: {Sum}")


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # create a list to loop over, a dict to store result, and a list to store samples
    pages_dict = {}
    pages_list = []
    samples = []
    for page in corpus:
        pages_dict[page] = 0
        pages_list.append(page)

    # first sample generated randomly
    previous = random.choice(pages_list)
    samples.append(previous)

    # do n-1 times of sampling
    for sample in range(n-1):
        # get a dict of possible pages and its pr
        possible_nexts = transition_model(corpus, previous, damping_factor)
        
        # choose the next page by considering its weight
        pages = list(possible_nexts.keys())
        weights = list(possible_nexts.values())
        next_page = random.choices(pages, weights, k=1)[0]
        samples.append(next_page)
        previous = next_page

    # loop over samples and count the times that we've landed on each page
    for p in samples:
        pages_dict[p] += 1
        
    # transfer counts into probability
    for p in pages_dict:
        pages_dict[p] = pages_dict[p] / n

    # check if sums to 1 and return result
    Sum = sum(pages_dict.values())
    if math.isclose(Sum, 1, rel_tol=1e-9):
        return pages_dict
    else:
        raise ValueError(f"Error in sample_pagerank. Wrong sum: {Sum}")
    
def pr_formula(corpus, p, pages_dict, damping_factor, N):
        # first calculate the sum of i
        Sum = 0
        iterations = []
        for page in corpus:
            if p in corpus[page]:
                 iterations.append(page)

        for i in iterations:
            Sum += (pages_dict[i] / len(corpus[i]))    

        # apply the formula
        pr_p = ((1 - damping_factor) / N) + damping_factor * Sum

        # return pr(p)
        return pr_p


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    N = len(corpus)

    # create a list and a dict to store pages
    pages_dict = {}
    pages_list = []
    modified_corpus = copy.deepcopy(corpus)

    for p in corpus:
        # assume every page's pr is 1/N initially
        pages_dict[p] = 1 / N
        pages_list.append(p)

        # if page has no outgoing link, interpret it as having a link for every page
        if not modified_corpus[p]:
            modified_corpus[p] = list(corpus.keys())

    # repeatingly updating page ranks until accurate
    repeat = True
    while repeat:
        repeat = False
        pages_dict_old = copy.deepcopy(pages_dict)

        # update each page's pr(p) in pages_dict
        for p in pages_list:
            pages_dict[p] = pr_formula(modified_corpus, p, pages_dict, damping_factor, N)
        
        # check if repeat or not
        for p in pages_dict:
            if abs(pages_dict_old[p] - pages_dict[p]) > 0.001:
                repeat = True
    return pages_dict


if __name__ == "__main__":
    main()
