# Python

## 动态语言
变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言，JavaScript是动态，Python也是动态。
在java中

 	int a=99;
 	int b=a;
 	a=110;
 	System.out.println("b="+b);
 	C c=new C();
 	c.a=88;
 	C cc=c;
 	c.a=22;
 	System.out.println("C cc.a="+cc.a);
	输出为
	b=99
	C cc.a=22

### 在文件前添加

	#!/usr/bin/env python
	# -*- coding: utf-8 -*-


### list,tuple。
tuple和list非常类似，但是tuple一旦初始化就不能修改。

	list:classmates = ['Michael', 'Bob', 'Tracy']
	tuple:classmates = ('Michael', 'Bob', 'Tracy').append().insert()
	.pop()//删除最后一个

### dict,set。


	d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
	s = set([1, 2, 3])//要创建一个set，需要提供一个list作为输入集合

### 参数
在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

默认参数一定是不可变的。None

可变参数就是传入tuple

关键字参数就是传入dict

比如定义一个函数，包含上述4种参数：

	def func(a, b, c=0, *args, **kw):
	print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw

### 迭代 

	for in ;
	for k, v in d.iteritems()；
	for i, value in enumerate(['A', 'B', 'C'])；

### 列表生成式，生成器。

## 类

	class Student(object):
    	def __init__(self, name, score):
    		self.name = name
    		self.score = score

如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。

## 继承

	class Animal(object):
		def run(self):

	class Dog(Animal):
	pass
	class Cat(Animal):
	pass









