from retrievecomments import RetrieveComments
from cleandata import cleanData

def main():
    youtubeUrl = 'https://www.youtube.com/watch?v=4wvS0DG0CHM'

    getComments = RetrieveComments(youtubeUrl)

    results = getComments.getComments()

    cleanData(results)


if __name__ == "__main__":
    main()