def word_count(file_name):
    
    word_count = {}

    for line in open(file_name):
        word_list = line.rstrip().split(' ')
        for word in word_list:
            word_count[word] = word_count.get(word,0) +1
    
    for word, count in word_count.items():
        print (word,count)

word_count('test.txt')
