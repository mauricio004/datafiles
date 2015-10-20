import string


class NewsStory(object):
    def __init__(self, guidx, titlex, subjectx, summaryx, linkx):
        """Creates a News Story"""
        self.guidx = guidx
        self.titlex = titlex
        self.subjectx = subjectx
        self.summaryx = summaryx
        self.linkx = linkx

    def getGuid(self):
        """Returns self's guid (globally unique identifier)"""
        return self.guidx

    def getTitle(self):
        """Returns self's title"""
        return self.titlex

    def getSubject(self):
        """"Returns self's subject"""
        return self.subjectx

    def getSummary(self):
        """Returns self's summary"""
        return self.summaryx

    def getLink(self):
        """Returns self's link (to more content)"""
        return self.linkx

    def __str__(self):
        return 'title:' + self.getTitle()


class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError


class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word

    def isWordIn(self, text):
        text_copy = text
        for c in text:
            if c in string.punctuation:
                text_copy = text_copy.replace(c, ' ')
        text_copy_list = text_copy.split(" ")
        isWord = False
        for w in text_copy_list:
            if self.word.lower() == w.lower():
                isWord = True
        return isWord


class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())


class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())


class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())


class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)


class AndTrigger(Trigger):
    def __init__(self, trigger, trigger2):
        self.trigger = trigger
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger.evaluate(story) and self.trigger2.evaluate(story)


class OrTrigger(Trigger):
    def __init__(self, trigger, trigger2):
        self.trigger = trigger
        self.trigger2 = trigger2

    def evaluate(self, story):
        return self.trigger.evaluate(story) or self.trigger2.evaluate(story)


class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, story):
        test = self.phrase in story.getTitle() or self.phrase in story.getSubject() or self.phrase in story.getSummary()
        return test


def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # This is a placeholder (we're just returning all the stories, with no filtering)
    list_stories = []
    for t in triggerlist:
        for s in stories:
            if t.evaluate(s) and s not in list_stories:
                list_stories.append(s)
    return list_stories


class TrueTrigger:
    def evaluate(self, story): return True

class FalseTrigger:
    def evaluate(self, story): return False


if __name__ == '__main__':
    t1 = PhraseTrigger("Neil deGrasse Tyson")
    t2 = OrTrigger(SummaryTrigger("Mars"), SummaryTrigger("Venus"))
    a = NewsStory('', 'Planetarium Popular', 'Strangely, children enjoy learning',
                  'Astrophysicist Neil deGrasse Tyson brings in new visitors to NYC museum', '')
    b = NewsStory('', 'NASA funding slashed', 'No future visits to Mars',
                  'Children sad at the loss of future jobs for astronauts', '')
    c = NewsStory('', 'Rover Visits the Red Planet', 'Curiosity picks up where Spirit left off',
                  'Findings reveal potential for life on Mars', '')
    d = NewsStory('', 'Uninhabitable Planets', 'Uranus, Neptune deemed too cold',
                  'Venus, Jupiter deemed much too toxic','')

    triggers = [t1, t2]
    stories = [a, b, c, d]
    fStories = filterStories(stories, triggers)



    for s in fStories:
        print s
    print
    pt = PhraseTrigger("New York City")
    a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
    b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
    c = NewsStory('', '', '', "asdfasfdNew York Cityasfdasdfasdf", '')
    noa = NewsStory('', "something something new york city", '', '', '')
    nob = NewsStory('', '', "something something new york city", '', '')
    noc = NewsStory('', '', '', "something something new york city", '')

    triggers2 = [pt]
    stories2 = [a, b, c, noa, nob, noc]
    fstories2 = filterStories(stories2, triggers2)

    for s2 in fstories2:
        print s2