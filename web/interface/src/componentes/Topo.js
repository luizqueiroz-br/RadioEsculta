import React from "react";
import logo from '../assest/logo.png'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faMap } from '@fortawesome/free-solid-svg-icons';


const ButtonNav = ({Icone, Nome, Rota}) =>{
    return(
       <div className="btn"> | <FontAwesomeIcon icon={faMap} /> {Nome} | </div>
    );
}


const Busca = () => {
    return(
            <div class="search-wrapper">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Search for..." />
                    <div class="input-group-append">
                        <button class="btn btn-outline-secondary search-button" type="button">
                            <i class="fas fa-search"></i>
                        </button>
                    </div>
                </div>
            </div>

        
    );
}


const Topo = ({projectName}) => {
return(
    <div  class="container content" >
    <div class="row">
    <nav class="navbar navbar-light bg-light">
        <div class="container">
        <a class="navbar-brand" href="/">
            <img src={logo} alt="" width="70" height="70"/> {projectName}
        </a>
        <ButtonNav Icone="fa-solid fa-map" Nome="Mapa" />
        <Busca />
        </div>
    </nav>
    </div>
        
</div>
);
}

export default Topo