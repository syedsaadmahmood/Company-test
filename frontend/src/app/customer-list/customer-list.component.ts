import { Component, OnInit } from '@angular/core';
import {DataService} from '../data.service';
import {Router} from '@angular/router';

declare var toastr: any;
@Component({
  selector: 'app-customer-list',
  templateUrl: './customer-list.component.html',
  styleUrls: ['./customer-list.component.css']
})
export class CustomerListComponent implements OnInit {
  usersData: any;

  constructor(private router: Router, private dataService: DataService) { }

  ngOnInit() {
    this.getUsers();
  }

  getUsers() {
    window.localStorage.setItem('loader', 'true');
    this.dataService.userList().subscribe(
      (data) => {
        console.log('users data', data);
        window.localStorage.setItem('loader', 'false');
        this.usersData = data;
        if (this.usersData.is_success === true) {
          this.usersData = this.usersData.data;
        } else {
          toastr.error(this.usersData.message);
        }
      },
      (error) => {
        window.localStorage.setItem('loader', 'false');
        console.log('error', error);
      }
    );
  }
}
