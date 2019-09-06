import pyspark
sc = pyspark.SparkContext('local[*]')

txt = sc.textFile('file:////usr/share/doc/python/copyright')
print("aaa >>> ", txt.count())
#      'This is text %s This is number %d'%(var_char,num1)

python_lines = txt.filter(lambda line: 'python' in line.lower())
print("bbb >>>> ", python_lines.count())
