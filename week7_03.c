#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <math.h>
#include <time.h>

typedef struct thread_data_s {
    double start;
    double end;
    double result;
} thread_data;

void* calculate (void *data) {
    thread_data* tdata = (thread_data*)data;
    int neg = 0;
    double start = tdata->start, end = tdata->end, result = 0.0;
    for (double i=start; i<=end; i+=2) {
        result += (1/i) * pow(-1, ++neg);
    }
    tdata->result += result;
}

int main () {
    pthread_t thread1, thread2, thread3;
    thread_data data1, data2, data3;

    struct timespec st = {0, 0};
    struct timespec et = {0, 0};

    data1.start = 3.0;
    data1.end = 22.0;
    data1.result = 0.0;

    data2.start = 23.0;
    data2.end = 42.0;
    data2.result = 0.0;

    data3.start = 43.0;
    data3.end = 62.0;
    data3.result = 0.0;

    clock_gettime(CLOCK_REALTIME, &st);
    pthread_create(&thread1, NULL, (void*)calculate, (void*)&data1);
    pthread_create(&thread2, NULL, (void*)calculate, (void*)&data2);
    pthread_create(&thread3, NULL, (void*)calculate, (void*)&data3);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    pthread_join(thread3, NULL);

    clock_gettime(CLOCK_REALTIME, &et);
    printf("%f\n", 4 * (1 + data1.result + data2.result + data3.result));
    printf("%ld ns\n",(et.tv_nsec-st.tv_nsec));

    /* -------------------------------------------------------------- */

    st.tv_sec = 0; st.tv_nsec = 0;
    et.tv_sec = 0; et.tv_nsec = 0; 
    clock_gettime(CLOCK_REALTIME, &st);

    double result2 = 0.0;
    int neg = 0;
    for (double i=3.0; i<=62.0; i+=2) {
        result2 += (1 / i) * pow(-1, (++neg));
    }
    printf("%f\n", 4 * (1 + result2));

    clock_gettime(CLOCK_REALTIME, &et);
    printf("%ld ns\n",(et.tv_nsec-st.tv_nsec));

    return 0;
}