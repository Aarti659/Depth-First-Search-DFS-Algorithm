
const dfs = function (Start, Target) {
    console.log("Visiting Node " + Start.value);
    if (Start.value === Target) {
       
        console.log("Found the node we're looking for!");
        return Start;
    }

    
    for (var j = 0; j < Start.children.length; j++) {
        var result = dfs(Start.children[j], Target);
        if (result != null) {
            
            return result;
        }
    }

   
    console.log("Went through all children of " + Start.value + ", returning to it's parent.");
    return null;
};

module.exports = {dfs};
