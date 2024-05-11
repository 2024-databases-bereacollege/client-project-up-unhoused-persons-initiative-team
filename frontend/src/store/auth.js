// store/auth.js
const authModule = {
  namespaced: true,
    state: {
      isAuthenticated: false,
      volunteer: null,
      hasRecordAccess: false, 
    },
    mutations: {
      setIsAuthenticated(state, value) {
        state.isAuthenticated = value;
      },
      setHasRecordAccess(state, hasRecordAccess) {
        state.hasRecordAccess = hasRecordAccess;
      },
    setVolunteer(state, volunteer) {
      state.volunteer = volunteer;
    },
    },
    actions: {
      setVolunteer({ commit }, volunteer) {
        commit('setVolunteer', volunteer);
      },
      setHasRecordAccess({ commit }, hasRecordAccess) {
        commit('setHasRecordAccess', hasRecordAccess);
      },
  
      login({ commit }) {
        // Perform login logic, e.g., send a request to the server
        // If login is successful, update the authentication state
        commit('setIsAuthenticated', true);
      },
      logout({ commit }) {
        // Perform logout logic, e.g., clear token, reset state
        commit('setIsAuthenticated', false);
      },
      // Other authentication-related actions
    },
    getters: {
      isAuthenticated: state => state.isAuthenticated,
      hasRecordAccess: state => state.hasRecordAccess,
    },
  };
  
  export default authModule;
