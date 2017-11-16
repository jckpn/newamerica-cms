import './../scss/all.scss';

import * as React from 'react';
import 'whatwg-fetch';
import 'url-polyfill';

window.React = React;

import composer from './react/index';
import actions from './react/actions';

class newamericadotorg {
  constructor(){
    this.composer = composer;
    this.store = composer.store;
    this.actions = actions;
  }
}

export default newamericadotorg;
