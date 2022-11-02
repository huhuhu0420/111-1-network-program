#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
void message(char *s) {
    for(int i=0;i<5;i++) {
    printf("%s", s);
    sleep(rand()%3); //單位秒
    // usleep(rand()%3); 單位微秒
    }
}
void thread(void) {
    message("The thread\n");
    pthread_exit(NULL); // 離開子執行緒
}
int main(){
    int i, p;
    time_t t;
    pthread_t id;
    srand((unsigned) time(&t));
    // 建立子執行緒
    p = pthread_create(&id, NULL,(void *) thread, NULL);
    if(p!=0){
        printf ("Create pthread error!n");
        exit(1);
    }
    message("The main\n");
    pthread_join(id, NULL); // 等待子執行緒執行完成
    return 0;
}
