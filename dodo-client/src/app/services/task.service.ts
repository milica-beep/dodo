import { HttpClient, HttpParams, withRequestsMadeViaParent } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TaskService {
  serverUrl:string = "http://127.0.0.1:5000/";

  constructor(private http: HttpClient) { }

  getLists() {
    return this.http.get<any>(this.serverUrl + "task/get-lists");
  }

  getTasks(parent: string) {
    let params = new HttpParams().set("parent", parent);
    return this.http.get<any>(this.serverUrl + "task/get-tasks", {params:params});
  }
  
  createNewList(listName: string) {
    return this.http.post<any>(this.serverUrl + "task/create-list", {'listName': listName});
  }

  completeTask(taskId: string, parent: string) {
    return this.http.patch<any>(this.serverUrl + "task/check-task", {'taskId': taskId, 'parent': parent});
  }

  createNewListTask(listId: string, task: string) {
    return this.http.post<any>(this.serverUrl + "task/create-list-task", {'listId': listId, 'task': task});
  }

  createNewDateTask(date: string, task: string) {
    return this.http.post<any>(this.serverUrl + "task/create-date-task", {'date': date, 'task': task});
  }

  deleteTask(taskId: string, parent: string) {
    let params = new HttpParams().set("taskId", taskId)
                                 .set("parent", parent);
    return this.http.delete<any>(this.serverUrl + 'task/delete-task', {params:params});
  }

  deleteList(listId: string) {
    let params = new HttpParams().set("listId", listId)
    return this.http.delete<any>(this.serverUrl + 'task/delete-list', {params:params});
  }
}
