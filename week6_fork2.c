#include <stdio.h> // f2.c
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
int main() {
    pid_t pid;
    int status, i;
    if(fork() == 0) {
        printf("child process pid =%d\n", getpid());
        // 第二版修改 lsxx 變成錯誤執行
        if(execlp("ls","ls_process","-l",NULL)<0){
            printf("after execlp fail, pid=%d\n", getpid());
            exit(8);
        }
        exit(6);
    }
    else {
        sleep(1);
        printf("Parent process, wait for child...\n");
        pid = wait(&status); //回傳等待的child程序的pid, 回傳值
        if (WIFEXITED(status)>0){
            printf("child's pid =%d, %d, exit status=%d\n", pid, WIFEXITED(status), WEXITSTATUS(status));
        }
        else
            printf("child's pid =%d, WIF status=%d\n", pid, WIFEXITED(status));
    }
    return 0;
}