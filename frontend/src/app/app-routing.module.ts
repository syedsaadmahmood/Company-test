import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {CustomerListComponent} from './customer-list/customer-list.component';
import {CustomerAddComponent} from './customer-add/customer-add.component';

const routes: Routes = [
  {path: '', component: CustomerListComponent},
  {path: 'customer/add', component: CustomerAddComponent},

  {path: '**', redirectTo: '' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})


export class AppRoutingModule { }
