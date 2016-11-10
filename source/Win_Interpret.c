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
#include <string.h>

void run (char *command);
void getDir (char* path,char* dir);

int main (int argc, char *argv[]){
	char dir[1024]; //the directory path
	char command[100]; //the command to be executed
	char* path; //the typical path variable
	path = getenv("PATH"); //get the environment PATH variable
	getDir(path,dir); //search for the right directory from PATH

	if (argc == 1){
		sprintf(command,"py \"%s\\Calcinter.py\"",dir);
		run(command);
	}else{
		sprintf(command,"py \"%s\\Calcinter.py\" \"%s\"",dir,argv[1]);
		run(command);
		getch();
	}
	return 0;
}

void run (char *command){
	system("TITLE Calculator Simple Language Interpreter");
	system(command);
}

void getDir (char* path,char* dir) {
	char *token;
	token = strtok(path,";");

	while (token != NULL){
		if(strstr(token, "CSL") != NULL || strstr(token, "csl") != NULL ) {
			strcpy(dir,token);
			break;
		}else{
			token = strtok(NULL,";");
		}
	}
}
