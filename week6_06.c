#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
    pid_t pid = fork();
    switch (pid)
    {
    case -1:
        fprintf(stderr, "error");
    case 0:
        printf("child process pid = %d\n", getpid());
        // sleep(10);
        printf("I am child\n");
        _exit(-60);
        break;
    default:
        printf("I am parent 1\n");
        sleep(2);
        printf("I am parent 2\n");
        int status;
        pid = wait(&status);
        int exitCode = WEXITSTATUS(status);
        printf("exit = %d\n", exitCode);
    }

    return 0;
}
