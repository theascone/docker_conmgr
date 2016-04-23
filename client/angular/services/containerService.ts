import {Inject, Injectable} from 'angular2/core';
import {Http} from 'angular2/http';
import {Observable} from 'rxjs/Observable';
import 'rxjs/add/operator/map'

import {Container} from '../shared/container';

@Injectable()
export class ContainerService {
  constructor(private http: Http) {}

  getContainers(): Observable<Container[]> {
    return this.http.get('/api/getContainers').map(response => {
        if (response.status == 200) {
          return response.json();
        } else {
          throw new Error();
        }
    });
  }

  startContainer(id: string): Observable<{}> {
    var req = {"id":id};
    return this.http.post('/api/startContainer', JSON.stringify(req)).map(response => {
      if (response.status == 200) {
        return {};
      } else {
        throw new Error();
      }
    });
  }

  stopContainer(id: string): Observable<{}> {
    var req = {"id":id};
    return this.http.post('/api/stopContainer', JSON.stringify(req)).map(response => {
      if (response.status == 200) {
        return {};
      } else {
        throw new Error();
      }
    });
  }
}
