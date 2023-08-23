-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: my_app
-- ------------------------------------------------------
-- Server version	5.7.20-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('6629488c7415');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chapter`
--

DROP TABLE IF EXISTS `chapter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chapter` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chapter`
--

LOCK TABLES `chapter` WRITE;
/*!40000 ALTER TABLE `chapter` DISABLE KEYS */;
INSERT INTO `chapter` VALUES (1,'Intro'),(2,'Operators and Expressions'),(3,'Logic'),(4,'Control flow'),(5,'Functions'),(6,'Srings');
/*!40000 ALTER TABLE `chapter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chapter_exercise`
--

DROP TABLE IF EXISTS `chapter_exercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chapter_exercise` (
  `exercise_id` int(11) NOT NULL,
  `chapter_id` int(11) NOT NULL,
  PRIMARY KEY (`exercise_id`,`chapter_id`),
  KEY `chapter_id` (`chapter_id`),
  CONSTRAINT `chapter_exercise_ibfk_1` FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`),
  CONSTRAINT `chapter_exercise_ibfk_2` FOREIGN KEY (`chapter_id`) REFERENCES `chapter` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chapter_exercise`
--

LOCK TABLES `chapter_exercise` WRITE;
/*!40000 ALTER TABLE `chapter_exercise` DISABLE KEYS */;
INSERT INTO `chapter_exercise` VALUES (5,1),(6,1),(2,2),(4,2),(1,3),(3,3),(12,4),(10,5),(7,6),(8,6),(9,6),(11,6);
/*!40000 ALTER TABLE `chapter_exercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chapter_lesson`
--

DROP TABLE IF EXISTS `chapter_lesson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chapter_lesson` (
  `chapter_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  PRIMARY KEY (`chapter_id`,`lesson_id`),
  KEY `chapter_lesson_fk2_idx` (`lesson_id`),
  CONSTRAINT `chapter_lesson_fk1` FOREIGN KEY (`chapter_id`) REFERENCES `chapter` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `chapter_lesson_fk2` FOREIGN KEY (`lesson_id`) REFERENCES `lesson` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chapter_lesson`
--

LOCK TABLES `chapter_lesson` WRITE;
/*!40000 ALTER TABLE `chapter_lesson` DISABLE KEYS */;
INSERT INTO `chapter_lesson` VALUES (1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),(1,10),(2,11),(2,12),(2,13),(2,14),(2,15),(2,16),(2,17),(4,18),(4,19),(4,20),(4,21),(4,22),(4,23),(4,24),(4,25);
/*!40000 ALTER TABLE `chapter_lesson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exercise`
--

DROP TABLE IF EXISTS `exercise`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exercise` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `content` mediumtext,
  `source_code` mediumtext,
  `default_elo_rating` float DEFAULT NULL,
  `solved_source_code` mediumtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exercise`
--

LOCK TABLES `exercise` WRITE;
/*!40000 ALTER TABLE `exercise` DISABLE KEYS */;
INSERT INTO `exercise` VALUES (1,'Sleep in','The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we\'re on vacation. Return True if we sleep in.','def sleep_in(weekday, vacation):   ',600,'\ntest_case = [(True, True), (False, False), (False, True), (True, False)]\n\ndef sleep_in(weekday, vacation):   \n	if not weekday or vacation:   \n		return True   \n	else:     \n		return False'),(2,'Sum double','Given two int values, return their sum. Unless the two values are the same, then return double their sum.','def sum_double(a,b):',600,'\ntest_case = [(1,2),(1,3),(1000,-100),(20,20),(0,0),(100,100)]\n\ndef sum_double(a, b):\n  # Store the sum in a local variable\n  sum = a + b\n  \n  # Double it if a and b are the same\n  if a == b:\n    sum = sum * 2\n  return sum'),(3,'Monkey Trouble','We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.','def monkey_trouble(a_smile, b_smile):   ',600,'\ntest_case = [(False,False),(True,True),(True,False),(False,True)]\n\ndef monkey_trouble(a_smile, b_smile):\n  if a_smile and b_smile:\n    return True\n  if not a_smile and not b_smile:\n    return True\n  return False\n  '),(4,'Makes10','Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.','def makes10(a, b):\n  \n',600,'\ntest_case = [(10,2),(9,9),(4,5),(5,6),(4,6),(-2,12)]\n\ndef makes10(a, b):\n  return (a == 10 or b == 10 or a+b == 10)\n  '),(5,'Parrot Trouble','We have a loud talking parrot. \nThe \"hour\" parameter is the current hour time in the range 0..23. \nWe are in trouble if the parrot is talking and the hour is before 7 or after 20. \nReturn True if we are in trouble.','def parrot_trouble(talking, hour):\n  \n',600,'\ntest_case = [(True,10),(True,2),(False,2),(True,20),(False,21),(True,0)]\n\ndef parrot_trouble(talking, hour):\n  return (talking and (hour < 7 or hour > 20))\n  \n'),(6,'Near Hundred','Given an int n, return True if it is within 10 of 100 or 200. \nNote: abs(num) computes the absolute value of a number.','def near_hundred(n):\n\n',1500,'\n\ntest_case = [(90,),(80,),(20,),(30,),(510,),(99,)]\n\ndef near_hundred(n):\n  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))\n \n'),(7,'Not String','Given a string, return a new string where \"not \" has been added to the front. \nHowever, if the string already begins with \"not\", return the string unchanged. .','def not_string(str):\n\n',1500,'\ntest_case = [(\"not\",),(\"notanot\",),(\"parrot\",),(\"hello\",),(\"notfunnyman\",)]\n\ndef not_string(str):\n  if len(str) >= 3 and str[:3] == \"not\":\n    return str\n  return \"not \" + str\n'),(8,'String Times','Given a string and a non-negative int n, return a larger string that is n copies of the original string.','def string_times(str, n):\n  \n',1700,'\ntest_case = [(\"not\",2),(\"notanot\",4),(\"parrot\",1),(\"hello\",5),(\"notfunnyman\",6)]\n\ndef string_times(str, n):\n  result = \"\"\n  for i in range(n):  # range(n) is [0, 1, 2, .... n-1]\n    result = result + str  # could use += here\n  return result\n'),(9,'Hello Name','Given a string name, e.g. \"Bob\", return a greeting of the form \"Hello Bob!\". ','def hello_name(name):\n  \n  \n',600,'\ntest_case = [(\"not\",),(\"notanot\",),(\"parrot\",),(\"hello\",),(\"notfunnyman\",)]\n\ndef hello_name(name):\n	return \"Hello \" + name;\n'),(10,'Make tags','The web is built with HTML strings like \"<i>Yay</i>\" which draws Yay as italic text. \nIn this example, the \"i\" tag makes <i> and </i> which surround the word \"Yay\". \nGiven tag and word strings, create the HTML string with tags around the word, e.g. \"<i>Yay</i>\". ','def make_tags(tag, word):\n  \n  \n',1100,'\n\ntest_case = [(\"i\",\"Huha\"),(\"quote\",\"To be or not to be\"),(\"p\",\"pp\"),(\"h19\",\"wOw\"),(\"i\",\"uh\")]\n\ndef make_tags(tag, word):\n	return \"<{0}>{1}</{0}>\".format(tag,word)\n\n'),(11,'First Two','Given a string, return the string made of its first two chars, so the String \"Hello\" yields \"He\". \nIf the string is shorter than length 2, return whatever there is, \nso \"X\" yields \"X\", and the empty string \"\" yields the empty string \"\". ','def first_two(str):\n  \n  \n',1000,'\ntest_case = [(\"123\",),(\"as\",),(\"adsasda\",),(\"1234\",),(\"0\",),(\"oo\",)]\n\ndef first_two(str):\n	if len(str) >= 2:\n		return str[:2]\n	else:\n		return str\n'),(12,'Cigar Party','When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. \nReturn True if the party with the given values is successful, or False otherwise.','def cigar_party(cigars, is_weekend):\n	\n  \n',800,'\n\ntest_case = [(30,False),(40,True),(90,False),(90,True),(45,True),(1,False)]\n \ndef func_resolved(cigars, is_weekend):\n    if is_weekend:\n        if cigars >= 40:\n            return True\n    elif cigars >= 40 and cigars <= 60:\n        return True\n \n    return False\n \n');
/*!40000 ALTER TABLE `exercise` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `homework`
--

DROP TABLE IF EXISTS `homework`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `homework` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(45) DEFAULT NULL,
  `content` mediumtext,
  `days_available` int(11) DEFAULT NULL,
  `default_points` int(11) DEFAULT NULL,
  `test_cases` mediumtext,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `homework`
--

LOCK TABLES `homework` WRITE;
/*!40000 ALTER TABLE `homework` DISABLE KEYS */;
INSERT INTO `homework` VALUES (1,'Homework 1','\nWrite a program which can compute the factorial of a given numbers.\nThe results should be printed in a comma-separated sequence on a single line.\nSuppose the following input is supplied to the program:\n8\nThen, the output should be:\n40320\n',14,200,'\r test_case = [(1,),(2,),(3,),(4,),(4,),(5,)]\r \r def fact(x):\r     if x == 0:\r         return 1\r     return x * func_resolved(x - 1)\r   \r   '),(2,'Homework 2','\nWrite a function to check whether a number is in a given range.\nThe function returns True or False.\nfunc(x,left_range,right_range)\n',7,80,'\ntest_case = [(1,0,10),(2,5,7),(3,1,2),(4,5,5),(4,0,10),(5,0,100)]\n\ndef is_in(a,b,c):\n	return a in range(b,c)\n  \n  '),(3,'Homework 3','\nWrite a function to check if a number is prime or not.\n',7,80,'\ntest_case = [(1,),(2,),(4,),(88,),(99,),(137,)]\n\ndef test_prime(n):\n    if (n==1):\n        return False\n    elif (n==2):\n        return True;\n    else:\n        for x in range(2,n):\n            if(n % x==0):\n                return False\n        return True\n  \n  '),(4,'Homework 4','\nWrite a Python program to reverse a string.\n',7,400,'\ntest_case = [(\"1231\",),(\"ana2\",),(\"mere4\",),(\"8844411\",),(\"aa9bb9cc\",),(\"123aa137\",)]\n\ndef string_reverse(str1):\n\n    rstr1 = \'\n    index = len(str1)\n    while index > 0:\n        rstr1 += str1[ index - 1 ]\n        index = index - 1\n    return rstr1\n  \n  ');
/*!40000 ALTER TABLE `homework` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lesson`
--

DROP TABLE IF EXISTS `lesson`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lesson` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) DEFAULT NULL,
  `content` mediumtext,
  `instructions` mediumtext,
  `source_code` mediumtext,
  `DEFAULT_ELO_RATING` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lesson`
--

LOCK TABLES `lesson` WRITE;
/*!40000 ALTER TABLE `lesson` DISABLE KEYS */;
INSERT INTO `lesson` VALUES (1,'Introduction','If all you know about a computer is how to turn it on and shut it down, no problem, here you will learn how to write code in the Python programming language, solving real world problems and getting the taste of coding really fast.\n\nWhat is Python?\n\n\nPython is probably one of the few programming languages which is both simple and powerful. This is good for beginners as well as for experts, and more importantly, is fun to program with. The next lessons will aim to help you learn this wonderful language and show how to get things done quickly and painlessly.','As you can see in the right there is a editor where you will write the Python code.\n\nPressing the \"Test\" button will immediately return your result in the console below the \"Submit\" button will send the code to our servers to evaluate your code and track your progress','# Do not be worry about all these symbols written here\n# We will get to the bottom of these asap\n# Just hit \"Submit\" for now!\n\nprint(\"Hello Friend!\")',100),(2,'Print statements','<p>A Python program is composed of statements.</p>\n<br>\n<p>Think of a statement as an instruction</p>\n<br>\n<p>\nIn our first program, we have only one statement: the <span class=\"source_code\">print</span> statement.\n</p>\n<br>\n\n<p>\n<span class=\"source_code\">print</span> is the function that displays something from your code\nto the computer, basically as you are saying to your computer \"Tell me this\", \"Tell me that\"<br>\nReplace \"Tell me\" with <span class=\"source_code\">print</span> and \"this\" with anything and you will<br>\nget <span class=\"source_code\">print(\"Anything you want to write\")</span> and you\'ve got your first program working<br>\n</p>\n\n\n','<p>In this statement, we call the print statement to which we supply the text \"hello\nworld\".</p><br>\n\n','#Go ahead, make the computer talk!',100),(3,'Basics','Just printing hello world is not enough, is it? You want to do more than that - you want to take some input, manipulate it and get something out of it. We can achieve this in Python using constants and variables, and we\'ll learn some other concepts as well in this chapter.','For now, just hit run and we will continue our lesson','print(\"Aleluia\")',100),(4,'Comments','Comments are any text to the right of the # symbol and is mainly useful as notes for the reader of the program.\n\nFor example:\n\nprint(\'hello world\') # Note that print is a function\n\nor:\n\n# Note that print is a function\nprint(\'hello world\')\nUse as many useful comments as you can in your program to:\n\n    explain assumptions\n    explain important decisions\n    explain important details\n    explain problems you\'re trying to solve\n    explain problems you\'re trying to overcome in your program, etc.\n','Code tells you how, comments should tell you why.\n\nThis is useful for readers of your program so that they can easily understand what the program is doing. Remember, that person can be yourself after six months!','#This is an example of a comment\n#Comment the line\'s below, or else, the code will produce an error\n\nThis means nothing to the computer, so you better comment it!\nRemember, computer\'s understand they\'re specific language, not human language.\nWell, maybe not yet!',250),(5,'Literal Constants','An example of a literal constant is a number like 5, 1.23, or a string like \'This is a string\' or \"It\'s a string!\".\n\nIt is called a literal because it is literal - you use its value literally. The number 2 always represents itself and nothing else - it is a constant because its value cannot be changed. Hence, all these are referred to as literal constants.','Go ahead and print any literal constans you consider!','#Remember the print, we\'ve learned a few lessons ago!',250),(6,'Numbers','Numbers are mainly of two types - integers and floats.\n\nAn example of an integer is 2 which is just a whole number.\n\nExamples of floating point numbers (or floats for short) are 3.23 and 52.3E-4. The E notation indicates powers of 10. In this case, 52.3E-4 means 52.3 * 10^-4^.','Let\'s print some numbers!','#print your age!\n\n\n\n#print how many eyes do you have\n\n\n\n#print your favourite number!',250),(7,'Strings','A string is a sequence of characters. Strings are basically just a bunch of words.\n\nYou will be using strings in almost every Python program that you write, so pay attention to the following part.\n\nSingle Quote\n\nYou can specify strings using single quotes such as \'Quote me on this\'.\n\nAll white space i.e. spaces and tabs, within the quotes, are preserved as-is.\nDouble Quotes\n\nStrings in double quotes work exactly the same way as strings in single quotes. An example is \"What\'s your name?\".','Print a string single quoted, then a string double quoted!','',250),(8,'Strings are immutable','This means that once you have created a string, you cannot change it. Although this might seem like a bad thing, it really isn\'t. We will see why this is not a limitation in the various programs that we see later on.','Print your name just to get to know you better!','',250),(9,'Variable','Using just literal constants can soon become boring - we need some way of storing any information and manipulate them as well. This is where variables come into the picture. Variables are exactly what the name implies - their value can vary, i.e., you can store anything using a variable. Variables are just parts of your computer\'s memory where you store some information. Unlike literal constants, you need some method of accessing these variables and hence you give them names.','Analyze the code, tested, modify it if you want and submit it!','# a variable can hold a number\n\na = 23\n\n#a variable can hold a string\n\nb = \"Hellooo\"\n\n#and they both can be printed!\n\nprint(a)\nprint(b)',200),(10,'Identifier Naming','Variables are examples of identifiers. Identifiers are names given to identify something. There are some rules you have to follow for naming identifiers:\n\n    The first character of the identifier must be a letter of the alphabet (uppercase ASCII or lowercase ASCII or Unicode character) or an underscore (_).\n    The rest of the identifier name can consist of letters (uppercase ASCII or lowercase ASCII or Unicode character), underscores (_) or digits (0-9).\n    Identifier names are case-sensitive. For example, myname and myName are not the same. Note the lowercase n in the former and the uppercase N in the latter.\n    Examples of valid identifier names are i, name_2_3. Examples of invalid identifier names are 2things, this is spaced out, my-name and >a1b2_c3.\n','Give a variable a value and print it to the console!','',300),(11,'Simple Math','This will be edited','sum two numbers and give it to the docker',' ',700),(12,'Your first operators','Most statements (logical lines) that you write will contain expressions. A simple example of an expression is 2 + 3. An expression can be broken down into operators and operands.  Operators are functionality that do something and can be represented by symbols such as + or by special keywords. Operators require some data to operate on and such data is called operands. In this case, 2 and 3 are the operands','Add two numbers and print them.',' ',700),(13,'Addition','The \"+\" symbol is reserved for adding stuff in python. Adding two numbers it\'s simple as 1+2+3. Just write this and print it. Just like in the same lesson, I know it\'s the same thing, but repeating is always a good practice!','Just add any kind of numbers and print them!',' ',700),(14,'Multiplying','You know that 2+2+2+2 it\'s basically 4 times adding a two? Haha, you know the drill!','Multiply some example, we are onto the big stuff!',' ',700),(15,'Divide and Subtract','Division is the evil brother of multiplying and subtract is the evil sister of addition. ','If i give you 6 - 3 / 3 , what is the answer? Just print that in the console!','#',700),(16,'The new one: MODULO','This is a frequent operator used in programming, it does so little, but it helps us developers so much. It\'s called module and it\'s symbol is \"%\". What the module does? It gives you the rest of the division of a number to another one. Examples: 5 % 2 = 1 (because 5 = 2 * 2 + 1, there is your 1)','How much is 11%10, 15%2, 15 % 3 and 100 % 99?',' ',900),(17,'Expressions','Another handy stuff in programming are the relational expressions. We need to define, check, constraint something to be somehow about another thing everytime! It\'s about the symbols \"<\", \">\" and \"==\". They tell us how big,small,equal is something in relation with something else.','Let\'s print some obvious relations, such as 2 < 3, 5>10 , 5 == 5, 5 >= 5, 10 < 4, 10 >4','# you will find the results are pretty human readable',1000),(18,'The if statement','The if statement is used to check a condition: if the condition is true, we run a block of statements (called the if-block), else we process another block of statements (called the else-block). The else clause is optional.','See the example below','if 2 == 2: print(\"2 is indeed equal to two\")',600),(19,'How the If works',' Often a computer program must make choices on which way to proceed, e.g., if the ball is in bounds, do one thing, else, do something different... if the data has all been processed, end the program, else continue to the next data item... while the player has lives left continue the game.  These \"things\" are called Conditions. Usually this is in the form of a mathematical statment using equals, less-than, or greater-than. ','Compare if a sum of two numbers equals another one and print it!',NULL,800),(20,'What ELSE can I say?','The ELSE keyword (else) let\'s you to run a piece of code if one of your if\'s it\'s not working.','Write something like: If this does not work, else do this!',NULL,1000),(21,'The while loop','The while statement allows you to repeatedly execute a block of statements as long as a condition is true. A while statement is an example of what is called a looping statement. A while statement can have an optional else clause.',NULL,'index = 0 while index < 10: print(\"Currently at step \" + index) index++',700),(22,'The FOR loop','The for..in statement is another looping statement which iterates over a sequence of objects i.e. go through each item in a sequence. We will see more about sequences in detail in later chapters. What you need to know right now is that a sequence is just an ordered collection of items.',NULL,'for i in range(1, 5):     print(i) else:     print(\'The for loop is over\')',700),(23,'The break Statement ','The break statement is used to break out of a loop statement i.e. stop the execution of a looping statement, even if the loop condition has not become False or the sequence of items has not been completely iterated over.  An important note is that if you break out of a for or while loop, any corresponding loop else block is not executed.',NULL,'i = 10 print(\'Final countdown: \') while True: 	if i == 0: 		print(\'Happy Birthday 2018!\')  	else: 		print(i)',800),(24,'The continue Statement ','The continue statement is used to tell Python to skip the rest of the statements in the current loop block and to continue to the next iteration of the loop.',NULL,'i = 10 while True: 	if i%2 == 0:		 		continue  	else: 		print(i)',900),(25,'Breaking down the loops','Write a program that runs 101 loops and at every 5 loops it prints \'Hello World\'',NULL,NULL,1200);
/*!40000 ALTER TABLE `lesson` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notification` (
  `user_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `content` varchar(250) DEFAULT NULL,
  `seen` tinyint(4) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`,`user_id`),
  KEY `user_notification_fk1_idx` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
INSERT INTO `notification` VALUES (18,'2018-06-04 14:18:35','Homework 2: 6 remaining days!',1,1),(18,'2018-06-04 14:18:36','Homework 2: 5 remaining days!',1,2),(18,'2018-06-04 14:18:35','Homework 2: 5 remaining days!',1,3),(18,'2018-06-04 14:18:36','Homework 2: 4 remaining days!',1,4),(18,'2018-06-04 14:18:35','Homework 2: 3 remaining days!',1,5),(18,'2018-06-04 14:18:36','Homework 2: 2 remaining days!',1,6),(18,'2018-06-04 14:19:11','Homework 2: 1 remaining days!',1,7),(18,'2018-06-04 14:19:12','Homework 2 expired!',1,8),(18,'2018-06-04 14:19:11','Homework 2 expired!',1,9),(18,'2018-06-04 15:31:40','Homework 2: 199 remaining days!',1,10),(18,'2018-06-04 15:31:40','Homework 2: 198 remaining days!',1,11),(18,'2018-06-04 15:31:40','Homework 2: 197 remaining days!',1,12),(18,'2018-06-04 17:29:56','Homework 2: 196 remaining days!',1,13),(18,'2018-06-04 17:29:57','Homework 2: 195 remaining days!',1,14),(18,'2018-06-04 17:29:56','Homework 2: 195 remaining days!',1,15),(18,'2018-06-04 17:29:57','Homework 2: 194 remaining days!',1,16),(18,'2018-06-04 17:29:56','Homework 2: 193 remaining days!',1,17),(18,'2018-06-04 17:29:57','Homework 2: 193 remaining days!',1,18),(18,'2018-06-04 17:29:56','Homework 2: 194 remaining days!',1,19),(18,'2018-06-04 17:29:57','Homework 2: 193 remaining days!',1,20),(18,'2018-06-04 17:32:40','Homework 2: 192 remaining days!',1,21),(18,'2018-06-04 17:32:41','Homework 2: 191 remaining days!',1,22),(18,'2018-06-04 17:32:40','Homework 2: 191 remaining days!',1,23),(18,'2018-06-04 17:32:41','Homework 2: 190 remaining days!',1,24);
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (2,'admin',NULL),(9,'user',NULL),(10,'user',NULL),(11,'user',NULL),(12,'user',NULL),(13,'user',NULL),(14,'user',NULL),(15,'user',NULL),(16,'user',NULL),(17,'user',NULL),(18,'user',NULL),(19,'user',NULL),(20,'user',NULL),(21,'user',NULL),(22,'user',NULL),(23,'user',NULL),(24,'user',NULL);
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(512) DEFAULT NULL,
  `elo_rating` float DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (18,NULL,'qwe123@gmail.com','$2b$12$BWr0VqR17XzKFkJDxBclNu579IUUl74nt4XVOSuGrDkpoaIjSZgrG',1192.57,NULL,20),(19,NULL,'diana123@gmail.com','$2b$12$cRa3NH48v7hqMVNvQkcJjO.2AU.xkFurupgnvuORGAbNk90vhw6SC',1200,NULL,21),(20,NULL,'adi123@gmail.com','$2b$12$yHmcTmJaI7yjkD4Ukti2XeWg.DvwAMOekd99Co0TKsoohqWBlSH6m',1200.02,NULL,22),(21,NULL,'ovidiu123@gmail.com','$2b$12$Pu9b9aP1I1p6RQM9a8fZwei6w1TdYZs3wzumciUQqa3tk5rP6to7G',1200.1,NULL,23),(22,NULL,'sun3@gmail.com','$2b$12$QsYaAfmfQBXtw.DyD6hu9.IFCjy/4ptcCFs6HdhbS/Wc/xQCe8CtC',1200.04,NULL,24);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_elo_update`
--

DROP TABLE IF EXISTS `user_elo_update`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_elo_update` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `elo_difference` float DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `notes` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_elo_update_fk1_idx` (`user_id`),
  CONSTRAINT `user_elo_update_fk1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_elo_update`
--

LOCK TABLES `user_elo_update` WRITE;
/*!40000 ALTER TABLE `user_elo_update` DISABLE KEYS */;
INSERT INTO `user_elo_update` VALUES (1,18,-24,'2018-06-04 18:50:02',NULL),(2,18,-9,'2018-06-04 18:59:39','Lesson 21'),(3,18,1,'2018-06-04 18:59:39','Lesson 21'),(4,18,0.525682,'2018-06-04 19:02:34','Lesson 22'),(5,18,-0.611245,'2018-06-04 19:17:48','Exercise Not String'),(6,22,0.0177492,'2018-06-04 22:27:45','Lesson Print statements'),(7,18,-9.10156,'2018-06-04 22:27:45','Lesson The break Statement '),(8,18,-0.581112,'2018-06-04 22:27:45','Exercise Not String');
/*!40000 ALTER TABLE `user_elo_update` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_exercise_difficulty`
--

DROP TABLE IF EXISTS `user_exercise_difficulty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_exercise_difficulty` (
  `user_id` int(11) NOT NULL,
  `exercise_id` int(11) NOT NULL,
  `elo_rating` float DEFAULT NULL,
  `completed` tinyint(4) DEFAULT NULL,
  `temporary_code` mediumtext,
  PRIMARY KEY (`user_id`,`exercise_id`),
  KEY `usr_ex_fk2_idx` (`exercise_id`),
  CONSTRAINT `usr_ex_fk1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `usr_ex_fk2` FOREIGN KEY (`exercise_id`) REFERENCES `exercise` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_exercise_difficulty`
--

LOCK TABLES `user_exercise_difficulty` WRITE;
/*!40000 ALTER TABLE `user_exercise_difficulty` DISABLE KEYS */;
INSERT INTO `user_exercise_difficulty` VALUES (18,1,599.694,1,NULL),(18,2,599.693,1,NULL),(18,3,602.11,1,NULL),(18,4,599.691,1,NULL),(18,5,609.193,1,NULL),(18,6,1492.14,1,NULL),(18,7,1501.58,0,'def not_string(str):\n    if str.startswith(\"not\"):\n        return str\n    else:\n        return \"not\"+str'),(18,9,599.505,1,NULL),(18,10,1095.12,1,NULL),(18,11,996.628,1,NULL),(18,12,798.877,1,NULL),(19,5,600,0,NULL),(20,5,600,0,NULL),(21,5,600,0,NULL),(22,5,600,0,'def parrot_trouble(talking, hour):\n  \n');
/*!40000 ALTER TABLE `user_exercise_difficulty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_homework_difficulty`
--

DROP TABLE IF EXISTS `user_homework_difficulty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_homework_difficulty` (
  `user_id` int(11) NOT NULL,
  `homework_id` int(11) NOT NULL,
  `points` int(11) DEFAULT NULL,
  `days_remaining` int(11) DEFAULT NULL,
  `expired` tinyint(4) DEFAULT NULL,
  `completed` tinyint(4) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `temporary_code` mediumtext,
  PRIMARY KEY (`user_id`,`homework_id`),
  KEY `user_hw_fk2_idx` (`homework_id`),
  CONSTRAINT `user_hw_fk1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `user_hw_fk2` FOREIGN KEY (`homework_id`) REFERENCES `homework` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_homework_difficulty`
--

LOCK TABLES `user_homework_difficulty` WRITE;
/*!40000 ALTER TABLE `user_homework_difficulty` DISABLE KEYS */;
INSERT INTO `user_homework_difficulty` VALUES (18,2,100,190,0,1,'2018-06-04 00:51:07','#nimicdef \ndef func(a,b,c):\n    return a in range(b,c)');
/*!40000 ALTER TABLE `user_homework_difficulty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_lesson_difficulty`
--

DROP TABLE IF EXISTS `user_lesson_difficulty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_lesson_difficulty` (
  `user_id` int(11) NOT NULL,
  `lesson_id` int(11) NOT NULL,
  `elo_rating` float NOT NULL,
  `COMPLETED` tinyint(1) DEFAULT '0',
  `temporary_code` mediumtext,
  PRIMARY KEY (`user_id`,`lesson_id`),
  KEY `lesson_id` (`lesson_id`),
  CONSTRAINT `user_lesson_difficulty_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`),
  CONSTRAINT `user_lesson_difficulty_ibfk_2` FOREIGN KEY (`lesson_id`) REFERENCES `lesson` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_lesson_difficulty`
--

LOCK TABLES `user_lesson_difficulty` WRITE;
/*!40000 ALTER TABLE `user_lesson_difficulty` DISABLE KEYS */;
INSERT INTO `user_lesson_difficulty` VALUES (18,1,99.9775,1,'print(2+2)'),(18,2,99.9775,1,NULL),(18,3,99.9765,1,NULL),(18,4,259.882,1,'print(1+2)'),(18,5,249.941,1,NULL),(18,6,249.941,1,NULL),(18,7,249.941,1,NULL),(18,8,249.941,1,NULL),(18,9,199.956,1,NULL),(18,10,299.922,1,NULL),(18,11,699.27,1,'print(2+2)'),(18,12,699.273,1,'print(2+2)'),(18,13,726.627,1,'print(2+2)'),(18,14,726.129,1,NULL),(18,15,699.043,1,NULL),(18,16,897.503,1,NULL),(18,17,996.316,1,NULL),(18,18,637.874,1,'if 2 == 2: print(\"2 is indeed equal to two\")'),(18,19,798.476,1,'print(1230)'),(18,20,996.584,1,NULL),(18,21,718.074,1,'a = 2;\nwhile(a != 0):\n    print(a)\n    a = a-1'),(18,22,699.474,1,'for i in range(10):\n    print(i)'),(18,23,809.102,0,'dsadsadsadsa'),(18,24,900,0,NULL),(18,25,1200,0,NULL),(19,1,100,0,NULL),(19,2,100,0,NULL),(19,3,100,0,NULL),(19,4,250,0,NULL),(19,5,250,0,NULL),(19,6,250,0,NULL),(19,7,250,0,NULL),(19,8,250,0,NULL),(19,9,200,0,NULL),(19,10,300,0,NULL),(19,11,700,0,NULL),(19,12,700,0,NULL),(19,13,700,0,NULL),(19,14,700,0,NULL),(19,15,700,0,NULL),(19,16,900,0,NULL),(19,17,1000,0,NULL),(19,18,600,0,NULL),(19,19,800,0,NULL),(19,20,1000,0,NULL),(19,21,700,0,NULL),(19,22,700,0,NULL),(19,23,800,0,NULL),(19,24,900,0,NULL),(19,25,1200,0,NULL),(20,1,99.9822,1,NULL),(20,2,100,0,NULL),(20,3,100,0,NULL),(20,4,250,0,NULL),(20,5,250,0,NULL),(20,6,250,0,NULL),(20,7,250,0,NULL),(20,8,250,0,NULL),(20,9,200,0,NULL),(20,10,300,0,NULL),(20,11,700,0,NULL),(20,12,700,0,NULL),(20,13,700,0,NULL),(20,14,700,0,NULL),(20,15,700,0,NULL),(20,16,900,0,NULL),(20,17,1000,0,NULL),(20,18,600,0,NULL),(20,19,800,0,NULL),(20,20,1000,0,NULL),(20,21,700,0,NULL),(20,22,700,0,NULL),(20,23,800,0,NULL),(20,24,900,0,NULL),(20,25,1200,0,NULL),(21,1,99.9822,1,NULL),(21,2,99.9823,1,NULL),(21,3,99.9823,1,NULL),(21,4,249.958,1,NULL),(21,5,250,0,NULL),(21,6,250,0,NULL),(21,7,250,0,NULL),(21,8,250,0,NULL),(21,9,200,0,NULL),(21,10,300,0,NULL),(21,11,700,0,NULL),(21,12,700,0,NULL),(21,13,700,0,NULL),(21,14,700,0,NULL),(21,15,700,0,NULL),(21,16,900,0,NULL),(21,17,1000,0,NULL),(21,18,600,0,NULL),(21,19,800,0,NULL),(21,20,1000,0,NULL),(21,21,700,0,NULL),(21,22,700,0,NULL),(21,23,800,0,NULL),(21,24,900,0,NULL),(21,25,1200,0,NULL),(22,1,99.9822,1,'# Do not be worry about all these symbols written here\n# We will get to the bottom of these asap\n# Just hit \"Submit\" for now!\n\nprint(\"Hello ma Friend!\")'),(22,2,99.9823,1,'#Go ahead, make the computer talk!\nprint(2)'),(22,3,100,0,'print(\"Aleluia\")'),(22,4,250,0,'#This is an example of a comment\n#Comment the line\'s below, or else, the code will produce an error\n\nThis means nothing to the computer, so you better comment it!\nRemember, computer\'s understand they\'re specific language, not human language.\nWell, maybe not yet!'),(22,5,250,0,'#Remember the print, we\'ve learned a few lessons ago!'),(22,6,250,0,'#print your age!\n\n\n\n#print how many eyes do you have\n\n\n\n#print your favourite number!'),(22,7,250,0,''),(22,8,250,0,''),(22,9,200,0,'# a variable can hold a number\n\na = 23\n\n#a variable can hold a string\n\nb = \"Hellooo\"\n\n#and they both can be printed!\n\nprint(a)\nprint(b)'),(22,10,300,0,''),(22,11,700,0,' '),(22,12,700,0,' '),(22,13,700,0,' '),(22,14,700,0,' '),(22,15,700,0,'#'),(22,16,900,0,' '),(22,17,1000,0,'# you will find the results are pretty human readable'),(22,18,600,0,'if 2 == 2: print(\"2 is indeed equal to two\")'),(22,19,800,0,NULL),(22,20,1000,0,NULL),(22,21,700,0,'index = 0 while index < 10: print(\"Currently at step \" + index) index++'),(22,22,700,0,'for i in range(1, 5):     print(i) else:     print(\'The for loop is over\')'),(22,23,800,0,'i = 10 print(\'Final countdown: \') while True: 	if i == 0: 		print(\'Happy Birthday 2018!\')  	else: 		print(i)'),(22,24,900,0,'i = 10 while True: 	if i%2 == 0:		 		continue  	else: 		print(i)'),(22,25,1200,0,NULL);
/*!40000 ALTER TABLE `user_lesson_difficulty` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-05 18:57:29
