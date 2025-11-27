(() => {
  const CHAMPIONS_PER_PAGE = 8;

  const champions = [
    {
      id: 'ahri',
      name: 'Ahri',
      title: 'the Nine-Tailed Fox',
      tags: ['Mage', 'Assassin'],
      info: { attack: 3, defense: 4, magic: 8, difficulty: 6 },
      stats: { hp: 590, mp: 418, armor: 21, spellblock: 30, attackdamage: 53, attackspeed: 0.668 },
      blurb:
        'Ahri is a mage who manipulates emotions, charming foes before finishing them with bursts of magic.',
      image: 'assets/images/champions/ahri.jpg'
    },
    {
      id: 'ashe',
      name: 'Ashe',
      title: 'the Frost Archer',
      tags: ['Marksman', 'Support'],
      info: { attack: 7, defense: 3, magic: 2, difficulty: 4 },
      stats: { hp: 640, mp: 280, armor: 26, spellblock: 30, attackdamage: 59, attackspeed: 0.658 },
      blurb:
        'Ashe leads the north with poise, volleying frost-tipped arrows that slow enemies and scout the Rift.',
      image: 'assets/images/champions/ashe.jpg'
    },
    {
      id: 'garen',
      name: 'Garen',
      title: 'the Might of Demacia',
      tags: ['Fighter', 'Tank'],
      info: { attack: 7, defense: 7, magic: 1, difficulty: 2 },
      stats: { hp: 690, mp: 0, armor: 36, spellblock: 32, attackdamage: 69, attackspeed: 0.625 },
      blurb: 'With unbreakable courage, Garen spins through the frontline while delivering decisive justice.',
      image: 'assets/images/champions/garen.jpg'
    },
    {
      id: 'lux',
      name: 'Lux',
      title: 'the Lady of Luminosity',
      tags: ['Mage', 'Support'],
      info: { attack: 2, defense: 4, magic: 9, difficulty: 5 },
      stats: { hp: 560, mp: 480, armor: 19, spellblock: 30, attackdamage: 54, attackspeed: 0.669 },
      blurb: 'Lux bends light into snares and beams, controlling fights with dazzling precision.',
      image: 'assets/images/champions/lux.jpg'
    },
    {
      id: 'leona',
      name: 'Leona',
      title: 'the Radiant Dawn',
      tags: ['Tank', 'Support'],
      info: { attack: 4, defense: 8, magic: 3, difficulty: 4 },
      stats: { hp: 640, mp: 302, armor: 47, spellblock: 32, attackdamage: 60, attackspeed: 0.625 },
      blurb: 'Leona shields her team with sunlight-forged armor, diving first and locking enemies in place.',
      image: 'assets/images/champions/leona.jpg'
    },
    {
      id: 'yasuo',
      name: 'Yasuo',
      title: 'the Unforgiven',
      tags: ['Fighter', 'Assassin'],
      info: { attack: 8, defense: 4, magic: 4, difficulty: 10 },
      stats: { hp: 630, mp: 0, armor: 30, spellblock: 32, attackdamage: 66, attackspeed: 0.69 },
      blurb: 'Yasuo dashes between foes, building storms that launch enemies skyward for lethal combos.',
      image: 'assets/images/champions/yasuo.jpg'
    },
    {
      id: 'ekko',
      name: 'Ekko',
      title: 'the Boy Who Shattered Time',
      tags: ['Assassin', 'Fighter'],
      info: { attack: 5, defense: 3, magic: 7, difficulty: 8 },
      stats: { hp: 655, mp: 280, armor: 32, spellblock: 32, attackdamage: 62, attackspeed: 0.688 },
      blurb: 'Ekko rewinds danger, diving deep before rewinding to safety with explosive damage.',
      image: 'assets/images/champions/ekko.jpg'
    },
    {
      id: 'vi',
      name: 'Vi',
      title: 'the Piltover Enforcer',
      tags: ['Fighter'],
      info: { attack: 7, defense: 5, magic: 3, difficulty: 4 },
      stats: { hp: 655, mp: 295, armor: 30, spellblock: 32, attackdamage: 63, attackspeed: 0.644 },
      blurb: 'Vi charges through obstacles with hextech gauntlets, isolating priority targets with a punch.',
      image: 'assets/images/champions/vi.jpg'
    },
    {
      id: 'jinx',
      name: 'Jinx',
      title: 'the Loose Cannon',
      tags: ['Marksman'],
      info: { attack: 9, defense: 2, magic: 4, difficulty: 6 },
      stats: { hp: 630, mp: 245, armor: 26, spellblock: 30, attackdamage: 59, attackspeed: 0.625 },
      blurb: 'Jinx swaps weapons for chaos, blanketing fights with rockets and lightning-fast fire.',
      image: 'assets/images/champions/jinx.jpg'
    },
    {
      id: 'seraphine',
      name: 'Seraphine',
      title: 'the Starry-Eyed Songstress',
      tags: ['Support', 'Mage'],
      info: { attack: 2, defense: 3, magic: 9, difficulty: 5 },
      stats: { hp: 570, mp: 440, armor: 19, spellblock: 30, attackdamage: 55, attackspeed: 0.669 },
      blurb: 'Seraphine harmonizes shields and snares, amplifying her allies with every note.',
      image: 'assets/images/champions/seraphine.jpg'
    },
    {
      id: 'thresh',
      name: 'Thresh',
      title: 'the Chain Warden',
      tags: ['Support', 'Tank'],
      info: { attack: 5, defense: 6, magic: 6, difficulty: 7 },
      stats: { hp: 600, mp: 274, armor: 32, spellblock: 30, attackdamage: 56, attackspeed: 0.625 },
      blurb: 'Thresh controls space with hooks and lanterns, swinging fights with pick potential.',
      image: 'assets/images/champions/thresh.jpg'
    },
    {
      id: 'sejuani',
      name: 'Sejuani',
      title: 'Fury of the North',
      tags: ['Tank', 'Fighter'],
      info: { attack: 5, defense: 7, magic: 4, difficulty: 5 },
      stats: { hp: 650, mp: 400, armor: 34, spellblock: 32, attackdamage: 66, attackspeed: 0.688 },
      blurb: 'Sejuani stampedes into skirmishes, freezing groups with permafrost and glacial prisons.',
      image: 'assets/images/champions/sejuani.jpg'
    }
  ];

  const uniqueRoles = ['all', ...new Set(champions.flatMap((champion) => champion.tags))];

  const state = {
    champions,
    currentRole: 'all',
    currentSearch: '',
    currentSort: 'name-asc',
    currentPage: 1,
    loadingMeta: new Map()
  };

  const elements = {
    championList: document.getElementById('champion-list'),
    searchInput: document.getElementById('search-input'),
    clearSearch: document.getElementById('clear-search'),
    roleFilters: document.getElementById('role-filters'),
    championCount: document.getElementById('champion-count'),
    sortSelect: document.getElementById('sort-select'),
    backToTop: document.getElementById('back-to-top'),
    pagination: document.getElementById('pagination'),
    modalElement: document.getElementById('champion-modal'),
    modalTitle: document.getElementById('champion-modal-title'),
    modalBody: document.getElementById('champion-modal-body')
  };

  const championModal = new bootstrap.Modal(elements.modalElement);

  const escapeHtml = (value = '') =>
    String(value).replace(
      /[&<>"']/g,
      (char) =>
        ({
          '&': '&amp;',
          '<': '&lt;',
          '>': '&gt;',
          '"': '&quot;',
          "'": '&#39;'
        })[char]
    );

  const formatNumber = (value, decimals = 0) => (typeof value === 'number' ? value.toFixed(decimals) : value);

  const emphasizeThe = (text = '') => text.replace(/\bthe\b/gi, (match) => `T${match.slice(1).toLowerCase()}`);

  const getSplashUrl = (champion) => champion.image;

  const getLoadingMeta = (championId) => {
    if (state.loadingMeta.has(championId)) {
      return state.loadingMeta.get(championId);
    }
    const meta = { team: Math.random() > 0.5 ? 'blue' : 'red' };
    state.loadingMeta.set(championId, meta);
    return meta;
  };

  const buildRoleBadges = (tags) =>
    tags
      .map((tag) => {
        const safeTag = escapeHtml(tag);
        return `<span class="role-badge role-theme" data-role="${safeTag}">${safeTag}</span>`;
      })
      .join('');

  const buildPowerProfile = (info = {}) => {
    const stats = [
      { label: 'Attack', value: info.attack },
      { label: 'Defense', value: info.defense },
      { label: 'Magic', value: info.magic },
      { label: 'Difficulty', value: info.difficulty }
    ];
    return stats
      .map(({ label, value = 0 }) => {
        const safeLabel = escapeHtml(label);
        const safeValue = Number(value) || 0;
        const percent = Math.max(0, Math.min(100, (safeValue / 10) * 100));
        return `
          <div class="mb-3">
            <div class="d-flex justify-content-between stat-meta mb-1">
              <span>${safeLabel}</span>
              <span>${safeValue}/10</span>
            </div>
            <div class="stat-bar">
              <div class="stat-fill" style="width: ${percent}%;"></div>
            </div>
          </div>
        `;
      })
      .join('');
  };

  const buildBaseStats = (stats = {}) => {
    const entries = [
      { label: 'HP', value: formatNumber(stats.hp, 0) },
      { label: 'MP', value: formatNumber(stats.mp, 0) },
      { label: 'Armor', value: formatNumber(stats.armor, 0) },
      { label: 'MR', value: formatNumber(stats.spellblock, 0) },
      { label: 'Attack Damage', value: formatNumber(stats.attackdamage, 0) },
      { label: 'Attack Speed', value: formatNumber(stats.attackspeed, 2) }
    ];

    return `
      <div class="row g-3">
        ${entries
          .map(
            ({ label, value }) => `
              <div class="col-6">
                <div class="mini-stat h-100">
                  <p class="mini-stat-label mb-1">${escapeHtml(label)}</p>
                  <p class="mini-stat-value mb-0">${escapeHtml(String(value ?? '—'))}</p>
                </div>
              </div>
            `
          )
          .join('')}
      </div>
    `;
  };

  const buildDetailContent = (champion) => {
    const safeName = escapeHtml(champion.name);
    const safeTitle = escapeHtml(emphasizeThe(champion.title));
    const safeBlurb = escapeHtml(champion.blurb || 'No lore available right now.').replace(/\n/g, '<br>');
    const roles = buildRoleBadges(champion.tags);
    const splash = getSplashUrl(champion);

    return `
      <div class="detail-hero mb-4">
        <img src="${splash}" alt="${safeName} splash art" class="w-100" loading="lazy">
      </div>
      <div class="detail-grid">
        <section class="detail-card">
          <p class="detail-section-title mb-2">${safeTitle}</p>
          <h2 class="mb-3">${safeName}</h2>
          <p class="detail-description mb-4">${safeBlurb}</p>
          <div class="d-flex flex-wrap gap-2">${roles}</div>
        </section>
        <section class="detail-card">
          <p class="detail-section-title mb-3">Power profile</p>
          ${buildPowerProfile(champion.info)}
        </section>
        <section class="detail-card">
          <p class="detail-section-title mb-3">Base stats</p>
          ${buildBaseStats(champion.stats)}
        </section>
      </div>
    `;
  };

  const showChampionDetail = (champion) => {
    if (!champion) return;
    const emphasizedTitle = emphasizeThe(champion.title);
    elements.modalTitle.textContent = `${champion.name} - ${emphasizedTitle}`;
    elements.modalBody.innerHTML = buildDetailContent(champion);
    championModal.show();
  };

  const getChampionFromElement = (element) => {
    const container = element?.closest('[data-champion-id]');
    if (!container) return null;
    const { championId } = container.dataset;
    return state.champions.find(({ id }) => id === championId);
  };

  const handleChampionView = (sourceElement) => {
    const champion = getChampionFromElement(sourceElement);
    showChampionDetail(champion);
  };

  const createCard = (champion) => {
    const safeName = escapeHtml(champion.name);
    const safeTitle = escapeHtml(champion.title);
    const roles = buildRoleBadges(champion.tags);
    const splash = getSplashUrl(champion);
    const { team } = getLoadingMeta(champion.id);

    return `
      <div class="loading-slot" data-team="${team}">
        <article class="slot-card" role="button" tabindex="0" data-champion-id="${champion.id}" aria-label="Preview ${safeName} details">
          <div class="slot-art" style="--splash-image: url('${splash}');">
            <img src="${splash}" alt="${safeName} splash art" loading="lazy">
          </div>
          <div class="slot-gradient"></div>
          <div class="slot-overlay">
            <div class="slot-body">
              <p class="slot-title">${safeTitle}</p>
              <h3 class="slot-name">${safeName}</h3>
              <div>${roles}</div>
            </div>
            <button type="button" class="slot-indicator" data-champion-id="${champion.id}" aria-label="View details for ${safeName}">View details</button>
          </div>
        </article>
      </div>
    `;
  };

  const createRoleFilters = () => {
    elements.roleFilters.innerHTML = uniqueRoles
      .map(
        (role) => `
          <button type="button" class="filter-pill filter-theme ${role === state.currentRole ? 'active' : ''}" data-role-filter="${role}" data-role="${role}">
            ${role}
          </button>
        `
      )
      .join('');
  };

  const updateRoleFilterActive = (selectedRole) => {
    elements.roleFilters.querySelectorAll('.filter-pill').forEach((button) => {
      button.classList.toggle('active', button.dataset.roleFilter === selectedRole);
    });
  };

  const sortChampions = (list) => {
    const sorted = [...list];
    switch (state.currentSort) {
      case 'name-desc':
        return sorted.sort((a, b) => b.name.localeCompare(a.name));
      case 'difficulty-desc':
        return sorted.sort((a, b) => b.info.difficulty - a.info.difficulty);
      case 'difficulty-asc':
        return sorted.sort((a, b) => a.info.difficulty - b.info.difficulty);
      case 'name-asc':
      default:
        return sorted.sort((a, b) => a.name.localeCompare(b.name));
    }
  };

  const getFilteredChampions = () => {
    let filtered = state.champions;

    if (state.currentRole !== 'all') {
      filtered = filtered.filter(({ tags }) => tags.includes(state.currentRole));
    }

    if (state.currentSearch) {
      const search = state.currentSearch.toLowerCase();
      filtered = filtered.filter(({ name, title }) => name.toLowerCase().includes(search) || title.toLowerCase().includes(search));
    }

    return sortChampions(filtered);
  };

  const updateChampionCount = (start, end, total) => {
    if (!total) {
      elements.championCount.textContent = 'No champions found.';
      return;
    }
    elements.championCount.innerHTML = `Displaying <strong>${start}-${end}</strong> of <strong>${total}</strong> champions in lobby`;
  };

  const showNoResults = () => {
    elements.championList.innerHTML = `
      <div class="w-100 text-center py-5">
        <i class="fas fa-search fa-3x text-secondary mb-3"></i>
        <p class="no-results h5">No champions match those filters.</p>
        <button class="btn btn-outline-warning mt-3" type="button" data-reset-filters>Reset Filters</button>
      </div>
    `;
  };

  const renderPagination = (totalPages) => {
    if (totalPages <= 1) {
      elements.pagination.innerHTML = '';
      return;
    }

    const { currentPage } = state;
    const maxVisible = 5;
    let startPage = Math.max(1, currentPage - Math.floor(maxVisible / 2));
    let endPage = Math.min(totalPages, startPage + maxVisible - 1);

    if (endPage - startPage + 1 < maxVisible) {
      startPage = Math.max(1, endPage - maxVisible + 1);
    }

    const parts = [];
    parts.push(`
      <button class="page-btn" data-page="${currentPage - 1}" ${currentPage === 1 ? 'disabled' : ''} aria-label="Previous page">
        <i class="fas fa-chevron-left"></i>
      </button>
    `);

    if (startPage > 1) {
      parts.push('<button class="page-btn" data-page="1">1</button>');
      if (startPage > 2) {
        parts.push('<span class="page-info">...</span>');
      }
    }

    for (let page = startPage; page <= endPage; page += 1) {
      parts.push(`
        <button class="page-btn ${page === currentPage ? 'active' : ''}" data-page="${page}">
          ${page}
        </button>
      `);
    }

    if (endPage < totalPages) {
      if (endPage < totalPages - 1) {
        parts.push('<span class="page-info">...</span>');
      }
      parts.push(`<button class="page-btn" data-page="${totalPages}">${totalPages}</button>`);
    }

    parts.push(`
      <button class="page-btn" data-page="${currentPage + 1}" ${currentPage === totalPages ? 'disabled' : ''} aria-label="Next page">
        <i class="fas fa-chevron-right"></i>
      </button>
    `);

    elements.pagination.innerHTML = parts.join('');
  };

  const renderChampions = () => {
    const filtered = getFilteredChampions();
    const total = filtered.length;

    if (!total) {
      updateChampionCount(0, 0, 0);
      showNoResults();
      elements.pagination.innerHTML = '';
      return;
    }

    const totalPages = Math.ceil(total / CHAMPIONS_PER_PAGE);
    if (state.currentPage > totalPages) {
      state.currentPage = 1;
    }

    const startIndex = (state.currentPage - 1) * CHAMPIONS_PER_PAGE;
    const endIndex = Math.min(startIndex + CHAMPIONS_PER_PAGE, total);
    const pageItems = filtered.slice(startIndex, endIndex);

    updateChampionCount(startIndex + 1, endIndex, total);
    elements.championList.innerHTML = pageItems.map(createCard).join('');
    renderPagination(totalPages);
  };

  const goToPage = (page) => {
    const totalItems = getFilteredChampions().length;
    const totalPages = totalItems ? Math.ceil(totalItems / CHAMPIONS_PER_PAGE) : 0;
    if (page < 1 || page > totalPages) return;
    state.currentPage = page;
    renderChampions();
    elements.championList.scrollIntoView({ behavior: 'smooth', block: 'start' });
  };

  const resetFilters = () => {
    state.currentRole = 'all';
    state.currentSearch = '';
    state.currentPage = 1;
    elements.searchInput.value = '';
    elements.clearSearch.classList.remove('visible');
    updateRoleFilterActive('all');
    renderChampions();
    elements.searchInput.focus();
  };

  const bindEvents = () => {
    elements.roleFilters.addEventListener('click', (event) => {
      const button = event.target.closest('[data-role-filter]');
      if (!button) return;
      state.currentRole = button.dataset.roleFilter;
      state.currentPage = 1;
      updateRoleFilterActive(state.currentRole);
      renderChampions();
    });

    let searchTimeout = null;
    elements.searchInput.addEventListener('input', (event) => {
      const value = event.target.value.trim();
      elements.clearSearch.classList.toggle('visible', value.length > 0);
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(() => {
        state.currentSearch = value;
        state.currentPage = 1;
        renderChampions();
      }, 250);
    });

    elements.clearSearch.addEventListener('click', resetFilters);

    elements.sortSelect.addEventListener('change', (event) => {
      state.currentSort = event.target.value;
      state.currentPage = 1;
      renderChampions();
    });

    window.addEventListener('scroll', () => {
      elements.backToTop.classList.toggle('visible', window.scrollY > 400);
    });

    elements.backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    elements.championList.addEventListener('click', (event) => {
      if (event.target.closest('[data-reset-filters]')) {
        resetFilters();
        return;
      }
      const indicator = event.target.closest('.slot-indicator');
      if (indicator) {
        handleChampionView(indicator);
      }
    });

    elements.championList.addEventListener('keydown', (event) => {
      const card = event.target.closest('.slot-card');
      if (!card) return;
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        handleChampionView(card);
      }
    });

    elements.pagination.addEventListener('click', (event) => {
      const button = event.target.closest('[data-page]');
      if (!button || button.disabled) return;
      const targetPage = Number(button.dataset.page);
      if (!Number.isNaN(targetPage)) {
        goToPage(targetPage);
      }
    });
  };

  const init = () => {
    createRoleFilters();
    bindEvents();
    renderChampions();
  };

  init();
})();
