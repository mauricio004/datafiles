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
        return self. subjectx

    def getSummary(self):
        """Returns self's summary"""
        return self.summaryx

    def getLink(self):
        """Returns self's link (to more content)"""
        return self.linkx


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


if __name__ == '__main__':
    #wt = WordTrigger('soft')
    #test = wt.isWordIn("Soft's the new tsoft pink!")
    #print(test)
    #news = NewsStory('', "\"Soft!\" he exclaimed as he threw the football", '', '', '')
    #title_triger = TitleTrigger('soft')
    #test = title_triger.evaluate(news)
    pt = PhraseTrigger("New York City")
    a = NewsStory('', "asfdNew York Cityasfdasdfasdf", '', '', '')
    b = NewsStory('', '', "asdfasfdNew York Cityasfdasdfasdf", '', '')
    pt.evaluate(a)
    #print(pt.evaluate(b))