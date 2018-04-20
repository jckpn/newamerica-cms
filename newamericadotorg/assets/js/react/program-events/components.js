import { Fetch, Response } from '../components/API';
import { EventListItem } from '../components/Content';
import { Slider } from '../components/Carousel';
import { Component } from 'react';
import PropTypes from 'prop-types';

const EventCarousel = ({ response }) => (
  <section className="container--full-width program-block">
  	<div className="program-block__heading container--wide">
  		<h1 className="centered margin-bottom-5">Upcoming Events</h1>
  		<p className="program-heading__subheading subheading--h1 centered">
  			Political Reform program publications help to generate new ideas, voices, and technologies.
  		</p>
  	</div>
  	<section className={`program-events container--medium${response.results.length< 5 ? ' no-slide' : '' }`}>
      <Slider
        infinite={false}
        speed={500}
        slidesToShow={5}
        slideToScroll={5}
        responsive={[
          { breakpoint: 576, settings: { slidesToShow: 1, slidesToScroll: 1} },
          { breakpoint: 1020, settings: { slidesToShow: 3, slidesToScroll: 3} },
        ]}
        prevArrow={<div className="slider-arrow--left"></div>}
        nextArrow={<div className="slider-arrow--right"></div>}>
          {response.results.map((e,i)=>(
            <div>
              <EventListItem item={e} />
            </div>
          ))}
      </Slider>
    </section>
  	<div className="program-block__button-wrapper button-wrapper centered">
  		<a className="button transparent" href={`${location.pathname}events`}>View All Events</a>
  	</div>
  </section>

);

export class Events extends Component {

  render() {
    let { contentType, programId } = this.props
    let query = {};
    switch(contentType){
      case 'homepage':
        break;
      case 'program':
        query.program_id = programId;
        break;
      case 'subprogram':
        query.subprogram_id = programId;
    }
    return(
      <Fetch
        name="program.events"
        endpoint="event"
        component={EventCarousel}
        fetchOnMount={true}
        showLoading={true}
        renderIfNoResults={false}
        transition={true}
        initialQuery={{
          time_period: 'future',
          page_size: 15,
          ...query
        }}
      />
    );
  }
}