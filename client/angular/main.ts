///<reference path='../node_modules/angular2/typings/browser.d.ts'/>

import {bootstrap} from 'angular2/platform/browser';
import {HTTP_PROVIDERS} from 'angular2/http';
import {enableProdMode} from "angular2/core";

import {ConmgrComponent} from './components/conmgr';

enableProdMode();
bootstrap(ConmgrComponent, [ HTTP_PROVIDERS ]);
