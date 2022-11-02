#include <sys/types.h> // f0.c
#include <sys/wait.h>
#include <stdio.h>
#include <unistd.h>
int main() {
    pid_t pid;
    pid = fork(); //fork a child process

    //若 pid>0, 進入parent process, pid 表示child 的pid
    //若 pid==0, 進入child process

    if (pid < 0) { //error occurred
        fprintf(stderr, "Fork Failed");
        return 1;
    }
    else if (pid == 0) { // 處於 child process
        printf("0=> Child pid=%d\n", getpid());
    }
    else { // 處於 parent process
        wait(NULL); // parent wait child complete
        printf("1=> Child pid=%d\n", pid);
        printf("1=> parent pid=%d\n", getpid());
        printf("Child Complete\n");
    }
    return 0;
}