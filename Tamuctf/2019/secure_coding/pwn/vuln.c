#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void echo()
{
	printf("%s", "Enter a word to be echoed:\n");
	char buf[128];
	memset(buf,'\0',sizeof(buf));
	fgets(buf,sizeof(buf),stdin);
	printf("%s\n", buf);
}

int main()
{
	echo();
}
