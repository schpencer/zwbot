walk(document.body);

// DOM manipulation code by T.J Crowder
// https://stackoverflow.com/questions/5904914/
function walk(node) {
  var child, next;

  switch (node.nodeType) {
    case 1:  // Element
    case 9:  // Document
    case 11: // Document fragment
      child = node.firstChild;
      while (child) {
        next = child.nextSibling;
        walk(child);
        child = next;
      }
      break;
    case 3: // Text node
      handleText(node);
      break;
  }
}

// replace occurences of all three zero width characters with text descriptions
function handleText(textNode) 
{
	var v = textNode.nodeValue;
  v = v.replace(/[\u200b]/g, " ZWSP ");
  v = v.replace(/[\u200c]/g, " ZWNJ ");
  v = v.replace(/[\u200d]/g, " ZWJ ");
	textNode.nodeValue = v;
}
