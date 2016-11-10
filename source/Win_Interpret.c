/*
 * interpreter.c
 *
 * Description: This program interpret the CSL (Calculator Simple Language)
 * using the python interpreter it is just a way to run it through
 * command line instead of the python interpreter
 *
 *  Created on: Nov 10, 2016
 *      Author: Naji
 */

#include <stdio.h>
#include <stdlib.h>


void run (char *command);

int main (int argc, char *argv[]){
	char command[100];
	if (argc == 1){
		sprintf(command,"py Calcinter.py");
		run(command);
	}else{
		sprintf(command,"py Calcinter.py \"%s\"",argv[1]);
		run(command);
		getch();
	}
	return 0;
}

void run (char *command){
	system("TITLE Calculator Simple Language Interpreter");
	system(command);
}