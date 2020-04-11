window.onload = (function() {

	var addElements = function() {

		var txt = document.insertAdjacentHTML("<input type='button' class='button',value='Next Topic'>");
		var el;

		el = document.createElement('div');
		el.appendChild(txt);
		document.body.appendChild(el);

		// If we want newly injected elements to be watched, refresh ScrollWatch. It will re-query the dom and start watching new elements.
		swInstance.refresh();

	};

	var swInstance = new ScrollWatch({
		watch: 'div',
		infiniteScroll: true,
		infiniteOffset: 200,
		onInfiniteYInView: addElements
	});

})();
