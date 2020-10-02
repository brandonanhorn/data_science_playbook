# importing regex and nltk
import re, nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# importing Counter to get word counts for bag of words
from collections import Counter
# importing part-of-speech function for lemmatization
from part_of_speech import get_part_of_speech

text = """
    She packed my bags last night pre-flight
Zero hour nine A.M.
And I'm gonna be high as a kite by then
I miss the earth so much, I miss my wife
It's lonely out in space
On such a timeless flight
And I think it's gonna be a long long time
'Til touchdown brings me 'round again to find
I'm not the man they think I am at home
Oh, no, no, no.
I'm a rocket man
Rocket man burning out his fuse up here alone
And I think it's gonna be a long long time
'Til touchdown brings me 'round again to find
I'm not the man they think I am at home
Oh, no, no, no.
I'm a rocket man
Rocket man burning out his fuse up here alone
Mars ain't the kind of place to raise your kids
In fact it's cold as hell
And there's no one there to raise them if you did
And all this science I don't understand
It's just my job five days a week
A rocket man, a rocket man
And I think it's gonna be a long long time
'Til touchdown brings me 'round again to find
I'm not the man they think I am at home
Oh, no, no, no.
I'm a rocket man
Rocket man burning out his fuse up here alone
And I think it's gonna be a long long time
'Til touchdown brings me 'round again to find
I'm not the man they think I am at home
Oh, no, no, no.
I'm a rocket man
Rocket man burning out his fuse up here alone
And I think it's gonna be a long long time
And I think it's gonna be a long long time
And I think it's gonna be a long long time
And I think it's gonna be a long long time
And I think it's gonna be a long long time
And I think it's gonna be a long long time
And I think it's gonna be a long long time
And I think it's gonna be a long long time
    """

cleaned = re.sub('\W+', ' ', text)
tokenized = word_tokenize(cleaned)

stop_words = stopwords.words('english')
filtered = [word for word in tokenized if word not in stop_words]

normalizer = WordNetLemmatizer()
normalized = [normalizer.lemmatize(token, get_part_of_speech(token)) for token in filtered]

bag_of_looking_glass_words = Counter(normalized)
print(bag_of_looking_glass_words)

ecg_text = 'An electrocardiogram is used to record the electrical conduction through a person\'s heart. The readings can be used to diagnose cardiac arrhythmias.'

tokenized_by_word = word_tokenize(ecg_text)

print(tokenized_by_word)

tokenized_by_sentence = sent_tokenize(ecg_text)

print(tokenized_by_sentence)
