#!/bin/bash
  for i in jenkins docker git kubernetes teraform
do
	mkdir $i
	touch $i/file.txt
done

