/**
 * @license Highcharts JS v9.3.2 (2021-11-29)
 * @module highcharts/modules/data
 * @requires highcharts
 *
 * Data module
 *
 * (c) 2012-2021 Torstein Honsi
 *
 * License: www.highcharts.com/license
 */
'use strict';
import Highcharts from '../../Core/Globals.js';
import HttpUtilities from '../../Core/HttpUtilities.js';
import Data from '../../Extensions/Data.js';
var G = Highcharts;
// Functions
G.ajax = HttpUtilities.ajax;
G.getJSON = HttpUtilities.getJSON;
G.post = HttpUtilities.post;
// Classes
G.Data = Data;
G.HttpUtilities = HttpUtilities;
