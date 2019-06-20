import { Component, OnInit } from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {DataService} from '../data.service';

declare var toastr: any;
@Component({
  selector: 'app-customer-add',
  templateUrl: './customer-add.component.html',
  styleUrls: ['./customer-add.component.css']
})
export class CustomerAddComponent implements OnInit {

  user: any = {name: '', username: '', email: '', password: '', confirmPassword: '', contact_number: '', cover_letter: '', resume: ''};
  userData: any;
  constructor(private router: Router, private activatedRoute: ActivatedRoute, private dataService: DataService) { }

  ngOnInit() {
  }

  onAddUser() {

    this.dataService.addUser(this.user).subscribe(
      (data) => {
        console.log('users data', data);
        window.localStorage.setItem('loader', 'false');
        this.userData = data;
        this.router.navigate(['']);
      },
      (error) => {
        window.localStorage.setItem('loader', 'false');
        console.log('error', error);
      }
    );
  }

}
