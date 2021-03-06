import './index.scss';

import React, { Component } from 'react';
import store from '../cache';
const ID = 'cookies-notification';
const NAME = 'cookiesNotification';

class APP extends Component {
  constructor(props){
    super(props);
    this.state = {
      cookiesConsent: store.get('cookiesConsent') || window.user.isAuthenticated || false,
      hidden: true
    }

    setTimeout(()=>{
      this.setState({ hidden: false });
    }, 10000)
  }
  iunderstand = () => {
    store.set('cookiesConsent', true);
    this.setState({ cookiesConsent: true });
  }
  render(){
    if(this.state.cookiesConsent === true) return null;
    return(
      <div className={`cookies-notification ${this.state.hidden ? 'hidden' : ''}`}>
        <div className='container'>
          <div className='row'>
            <div className='col-12 col-md-8'>
              <h4 className="white margin-0">
                This website uses cookies to give you the best experience.
              </h4>
              <h6 className="white margin-0">
                By clicking "OK, I understand," you are giving your consent.
              </h6>
            </div>
            <div className='col-12 col-md-4 margin-top-10 margin-top-md-0'>
              <button className="button white" onClick={this.iunderstand}>OK, I understand</button>
              <h6 className="white inline"><a href='/policies-and-procedures/'>Read more</a></h6>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default { NAME, ID, APP }
