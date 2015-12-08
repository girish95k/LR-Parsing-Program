%option noyywrap
%{
	#include<stdio.h>
	int comments=0;
%}

%%
{
	"/*" {
		char prev=0;
		int done=0;
		char ch=input();
		while(!done) {
			if(ch=='*') prev=1;
			if(ch=='/' && prev==1 )done=1;
			else if(ch!='*')prev=0;
			ch=input();
			}
		comments++;
		}
	\/\/.* {
		comments++;
		}
	(.) {
		putchar(yytext[0]);
	}
}
%%
int main()
{
	printf("REMOVING...\n");
	//yyin=fopen("program.c","r");
	yyout=fopen("out.c","w");
	//printf(yyin);
	yylex();
	printf("No of comments : %d ",comments);
	return 0;
}