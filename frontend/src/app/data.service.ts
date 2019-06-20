import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {Constants} from './constants';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor(private http: HttpClient) { }

  userList() {
    const headerJson = {'Content-Type': 'application/json'};
    const headers = new HttpHeaders(headerJson);
    return this.http.get(Constants.apiAddress + '/user/operation/', {headers});
  }

  addUser(user) {
    const headerJson = {'Content-Type': 'application/json'};
    const headers = new HttpHeaders(headerJson);
    console.log('user', user);
    return this.http.post(Constants.apiAddress + '/user/operation/', JSON.stringify(user), {headers});
  }

}
