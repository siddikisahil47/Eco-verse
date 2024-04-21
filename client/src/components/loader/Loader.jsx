import React from 'react';
import './loader.css';

function Loader() {
    return (
        <section className="wrapper">
            <div className="loader">
                <div className="loading one"></div>
                <div className="loading two"></div>
                <div className="loading three"></div>
                <div className="loading four"></div>
            </div>
        </section>
    );
}

export default Loader;
