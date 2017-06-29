const Header = ({ page }) => (
  <header className='weekly-header'>
    <div className="container">
      <div className="row">
        <div className="col-3"><a href="/">
          <div className="weekly-header__logo logo sm white"></div></a>
        </div>
        <div className="weekly-header__title col-6">
          <div className="weekly-header__logo-wrapper">
            {/* <a href="/"><div className="weekly-header__logo logo white sm"></div></a> */}
          </div>
          <div className="weekly-header__title__wrapper">
            <a href="/weekly">
              <h4 className="weekly-header__heading no-margin">The Weekly</h4>
            </a>
          </div>
        </div>
        <div className="col-3"></div>
      </div>
    </div>
  </header>
);

export default Header;
