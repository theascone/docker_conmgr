import {Inject, Injectable} from 'angular2/core';
import {Http} from 'angular2/http';

import {Container} from '../shared/container';

@Injectable()
export class ContainerService {
  constructor(private http: Http) {}

  getContainers(): Promise<Container[]> {
    return Promise.reject<Container[]>({});
    //return Promise.resolve(CONTS);
    //return this.http.get('api/getContainers').toPromise().then(response => {
        //if (response.ok) {
        //  return response.json();
        //} else {
        //
        //}
    //});
  }

  startContainer(id: string): Promise<void> {
    var req = {"id":id};
    return this.http.post('api/startContainer', req.json());
  }

  stopContainer(id: string): Promise<void> {
    return new Promise<void>(resolve =>
        setTimeout(()=>resolve(), 2000) // 2 seconds
    );
  }
}

var CONTS: Container[] = [
  { "id": "4kghj23ghj3rhjr", "running":true, "name":"minecraft1", "info": "heey"},
  { "id": "4kghj23ghj3rhjr", "running":false, "name":"minecraft2", "info": "lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum"},
  { "id": "4kghj23ghj3rhjr", "running":false, "name":"minecraft3", "info": "heey thats petty good"}
]
