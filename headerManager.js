class SpecialHeader extends HTMLElement {
    ConnectedCallBack() {
        this.innerHTML = 
        `<nav class="navbar fixed-top navbar-expand-sm navbar-dark bg-dark">
        <div class="container">
        <a 
          href="#" 
          class="navbar-brand mb-0 h1">
          <img src="static/fifa_wc.svg"
          width="30" height "30">
          Flashback Footy
        </a>
        <button
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        class="navbar-toggler"
        data-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
          >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse"
        id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item active">
            <a href="#" class="nav-link active">
              Home
              </a>
          </li>
          <li class="nav-item dropdown">
            <a href="#" class="nav-link 
              dropdown-toggle"
              id="navbarDropdown" role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
              >
              World Cup Eras
            </a>
            <ul class="dropdown-menu" 
              aria-labelledby="navbarDropdown">
                <li><a href="worldcup.html" class="dropdown-item">All</a></li>
                <li><a href="#" class="dropdown-item">1930s</a></li>
                <li><a href="#" class="dropdown-item">1950s</a></li>
                <li><a href="#" class="dropdown-item">1960s</a></li>
                <li><a href="#" class="dropdown-item">1970s</a></li>
                <li><a href="#" class="dropdown-item">1980s</a></li>
                <li><a href="#" class="dropdown-item">1990s</a></li>
                <li><a href="#" class="dropdown-item">2000s</a></li>
                <li><a href="#" class="dropdown-item">2010s</a></li>
                <li><a href="#" class="dropdown-item">2020s</a></li>
              </ul>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link">
              Players
            </a>
          </li>
        </ul>
      </div>
      </div>
      </nav>`
    }
}

customElements.define('special-header',SpecialHeader)